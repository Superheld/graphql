import graphene
from graphene import ObjectType, String, Int, List, Mutation
from pony.orm import db_session
from models.mistralModel import User

class UserType(ObjectType):
    id = Int()
    name = String()
    email = String()

class CreateUser(Mutation):
    class Arguments:
        name = String(required=True)
        email = String(required=True)

    user = graphene.Field(lambda: UserType)

    @db_session
    def mutate(self, info, name, email):
        processed_name = name.strip().title()
        processed_email = email.strip().lower()
        user = User(name=processed_name, email=processed_email)
        return CreateUser(user=user)

class Query(ObjectType):
    users = List(UserType)

    @db_session
    def resolve_users(self, info):
        users = list(User.select())
        processed_users = [
            UserType(id=user.id, name=user.name.strip().title(), email=user.email.strip().lower())
            for user in users
        ]
        return processed_users

class Mutation(ObjectType):
    create_user = CreateUser.Field()