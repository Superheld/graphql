from pony.orm import Required, PrimaryKey, db_session, Optional, Set, select
from datetime import datetime
from . import db

class CategoryRelation(db.Entity):
    category1 = Required('Categories', reverse='related_categories')
    category2 = Required('Categories', reverse='related_to_categories')

class Categories(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    description = Required(str)
    isDeletedDate = Optional(datetime)

    related_categories = Set(CategoryRelation, reverse='category1')
    related_to_categories = Set(CategoryRelation, reverse='category2')

    @db_session
    def before_insert(self):
        self.name = self.name.strip().title()

    @db_session
    def mark_as_deleted(self):
        self.isDeletedDate = datetime.now()

    @staticmethod
    @db_session
    def get_all_active():
        return select(c for c in Categories if c.isDeletedDate is None)

    @staticmethod
    def get_all_categories():
        def recursive_get(category, result, visited):
            if category.id in visited:
                return
            visited.add(category.id)
            result.append({
                'id': category.id,
                'name': category.name,
                'description': category.description,
                'isDeletedDate': category.isDeletedDate,
            })
            for relation in category.related_categories:
                recursive_get(relation.category2, result, visited)

        root_categories = Categories.get_all_active()
        result = []
        visited = set()
        for category in root_categories:
            recursive_get(category, result, visited)
        return result