from tokenize import String

from graphene import ID, ObjectType, Int, Float, String, DateTime, Boolean
from graphene_sqlalchemy import SQLAlchemyObjectType
from db_models import *
import graphene

class Role(SQLAlchemyObjectType):
    id = ID()
    name = String(required=True)
    description = String()
    created_at = DateTime()
    updated_at = DateTime()


class State(SQLAlchemyObjectType):
    id = ID()
    name = String(required=True)
    abbreviation = String()
    created_at = DateTime()
    updated_at = DateTime()


class District(SQLAlchemyObjectType):
    id = ID()
    name = String(required=True)
    area = Float()
    state = State()
    created_at = DateTime()
    updated_at = DateTime()


class City(SQLAlchemyObjectType):
    id = ID()
    name = String(required=True)
    type = String()
    district = District()
    pincode = String()
    created_at = DateTime()
    updated_at = DateTime()


class Address(SQLAlchemyObjectType):
    id = ID()
    apt_house_name = String()
    street = String()
    town_city = City()
    created_at = DateTime()
    updated_at = DateTime()


class Product(SQLAlchemyObjectType):
    id = ID()
    name = String(required=True)
    price = Int()
    created_at = DateTime()
    updated_at = DateTime()


class User(SQLAlchemyObjectType):
    class Meta:
        model = UserModel
        interfaces = (graphene.relay.Node,)


class UserProfile(SQLAlchemyObjectType):
    id = ID()
    user = User()
    role = Role()
    created_at = DateTime()
    updated_at = DateTime()


class Shop(SQLAlchemyObjectType):
    id = ID()
    name = String(required=True)
    address = Address()
    owner = UserProfile()
    created_at = DateTime()
    updated_at = DateTime()


class ProductShop(SQLAlchemyObjectType):
    id = ID()
    product = Product()
    shop = Shop()
    price = Float()
    created_at = DateTime()
    updated_at = DateTime()


class TransactionType(SQLAlchemyObjectType):
    id = ID()
    type = String(required=True)  #CASH, CARD, DEBT
    created_at = DateTime()
    updated_at = DateTime()


class Transaction(SQLAlchemyObjectType):
    id = ID()
    buyer = UserProfile()
    product = ProductShop()
    amount = Float()
    type = TransactionType()
    created_at = DateTime()
    updated_at = DateTime()


class Debt(SQLAlchemyObjectType):
    id = ID()
    debiter = UserProfile()
    creditor = Shop()
    amount = Float()
    created_at = DateTime()
    updated_at = DateTime()
