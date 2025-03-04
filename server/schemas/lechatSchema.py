import graphene
from graphene import ObjectType, String, Int, Float, List, Mutation
from pony.orm import db_session
from models.lechatModel import Product

class ProductType(ObjectType):
    id = Int()
    name = String()
    price = Float()

class CreateProduct(Mutation):
    class Arguments:
        name = String(required=True)
        price = Float(required=True)

    product = graphene.Field(lambda: ProductType)

    @db_session
    def mutate(self, info, name, price):
        processed_name = name.strip().title()
        product = Product(name=processed_name, price=price)
        return CreateProduct(product=product)

class Query(ObjectType):
    products = List(ProductType)

    @db_session
    def resolve_products(self, info):
        products = list(Product.select())
        processed_products = [
            ProductType(id=product.id, name=product.name.strip().title(), price=product.price)
            for product in products
        ]
        return processed_products

class Mutation(ObjectType):
    create_product = CreateProduct.Field()