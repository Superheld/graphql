from pony.orm import Required, PrimaryKey, db_session
from . import db

class User(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    email = Required(str)

    @db_session
    def before_insert(self):
        self.name = self.name.strip().title()
        self.email = self.email.strip().lower()