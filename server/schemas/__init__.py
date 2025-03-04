from graphene import Schema
from .mistralSchema import Query as UserQuery, Mutation as UserMutation
from .lechatSchema import Query as ProductQuery, Mutation as ProductMutation

class Query(UserQuery, ProductQuery):
    pass

class Mutation(UserMutation, ProductMutation):
    pass

schema = Schema(query=Query, mutation=Mutation)