from tokenize import String

from graphene import ID, ObjectType, Int, Float, String, DateTime


class Role(ObjectType):
    id = ID()
    name = String(required=True)
    description = String()
    created_at = DateTime()
    updated_at = DateTime()


class State(ObjectType):
    id = ID()
    name = String(required=True)
    abbreviation = String()
    created_at = DateTime()
    updated_at = DateTime()


class District(ObjectType):
    id = ID()
    name = String(required=True)
    area = Float()
    state = State()
    created_at = DateTime()
    updated_at = DateTime()


class City(ObjectType):
    id = ID()
    name = String(required=True)
    type = String()
    district = District()
    pincode = String()
    created_at = DateTime()
    updated_at = DateTime()


class Address(ObjectType):
    id = ID()
    apt_house_name = String()
    street = String()
    town_city = City()
    created_at = DateTime()
    updated_at = DateTime()


class Product(ObjectType):
    id = ID()
    name = String(required=True)
    price = Int()
    created_at = DateTime()
    updated_at = DateTime()


class User(ObjectType):
    id = ID()
    username = String(required=True)
    fname = String()
    lname = String()
    email = String()
    password = String()
    #address = Address()
    created_at = DateTime()
    updated_at = DateTime()


class UserProfile(ObjectType):
    id = ID()
    user = User()
    role = Role()
    created_at = DateTime()
    updated_at = DateTime()


class Shop(ObjectType):
    id = ID()
    name = String(required=True)
    address = Address()
    owner = UserProfile()
    created_at = DateTime()
    updated_at = DateTime()


class ProductShop(ObjectType):
    id = ID()
    product = Product()
    shop = Shop()
    price = Float()
    created_at = DateTime()
    updated_at = DateTime()


class TransactionType(ObjectType):
    id = ID()
    type = String(required=True)  #CASH, CARD, DEBT
    created_at = DateTime()
    updated_at = DateTime()


class Transaction(ObjectType):
    id = ID()
    buyer = UserProfile()
    product = ProductShop()
    amount = Float()
    type = TransactionType()
    created_at = DateTime()
    updated_at = DateTime()


class Debt(ObjectType):
    id = ID()
    debiter = UserProfile()
    creditor = Shop()
    amount = Float()
    created_at = DateTime()
    updated_at = DateTime()
