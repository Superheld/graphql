import graphene
from graphene import ObjectType, String, Int, List, Mutation, DateTime
from pony.orm import db_session
from models.kategorienModel import Categories, CategoryRelation

class CategoryType(ObjectType):
    id = Int()
    name = String()
    description = String()
    is_deleted_date = DateTime()
    related_categories = List(lambda: CategoryType)

class CreateCategory(Mutation):
    class Arguments:
        name = String(required=True)
        description = String(required=True)
    category = graphene.Field(lambda: CategoryType)

    @db_session
    def mutate(self, name, description):
        category = Categories(name=name, description=description)
        return CreateCategory(category=category)

class DeleteCategory(Mutation):
    class Arguments:
        id = Int(required=True)

    success = graphene.Boolean()

    @db_session
    def mutate(self, id):
        category = Categories.get(id=id)
        if category:
            category.mark_as_deleted()
            return DeleteCategory(success=True)
        return DeleteCategory(success=False)

class CategoryRelationType(ObjectType):
    id = Int()
    category1 = graphene.Field(lambda: CategoryType)
    category2 = graphene.Field(lambda: CategoryType)

class AddCategoryRelation(Mutation):
    class Arguments:
        category1_id = Int(required=True)
        category2_id = Int(required=True)

    relation = graphene.Field(lambda: CategoryRelationType)

    @db_session
    def mutate(self, category1_id, category2_id):
        category1 = Categories.get(id=category1_id)
        category2 = Categories.get(id=category2_id)
        if category1 and category2:
            relation = CategoryRelation(category1=category1, category2=category2)
            return AddCategoryRelation(relation=relation)
        return None

class Query(ObjectType):
    categories = List(CategoryType)
    category = graphene.Field(CategoryType, id=Int())

    @db_session
    def resolve_categories(self, info):
        return Categories.get_all_categories()

    @db_session
    def resolve_category(self, info, id):
        return Categories.get(id=id)

class Mutation(ObjectType):
    create_category = CreateCategory.Field()
    delete_category = DeleteCategory.Field()
    add_category_relation = AddCategoryRelation.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)