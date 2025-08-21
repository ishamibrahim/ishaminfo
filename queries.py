import graphene
import requests
from graphene import ObjectType, Int, List, Field, String

from db_models import UserModel
from schema import Transaction, User, Product


class Query(ObjectType):
    transaction = graphene.Field(Transaction, transaction_id=Int(required=True))
    all_transactions = List(Transaction)
    users = List(User)
    user = Field(User, username=String(required=True))

    # All get operation methods have to start with the term 'resolve_'
    def resolve_transaction(self, info, transaction_id):
        # Fetch order data from order/sales service
        transaction_url = f"http://shop-service/transaction/{transaction_id}/"
        try:
            trans_response = requests.get(transaction_url)
            trans_response.raise_for_status()
            transaction_data = trans_response.json()

            # Fetch user data
            user_url = f"http://user-service/users/{transaction_data['buyer_id']}/"
            user_response = requests.get(user_url)
            user_response.raise_for_status()
            user_data = user_response.json()

            # Fetch products
            products_data = []
            for pid in transaction_data.get('product_ids', []):
                product_url = f"http://product-service/products/{pid}/"
                product_response = requests.get(product_url)
                product_response.raise_for_status()
                products_data.append(product_response.json())

            return Transaction(
                id=transaction_data['id'],
                user=User(
                    id=user_data['id'],
                    name=f"{user_data['fname']} {user_data['lname']}",
                    email=user_data['email']
                ),
                products=[Product(
                    id=p['id'],
                    name=p['name'],
                    price=p['price']
                ) for p in products_data]
            )
        except requests.RequestException as e:
            raise Exception(f"Error fetching order: {str(e)}")

    def resolve_all_transactions(self, info):
        return self.all_transactions

    def resolve_users(self,  info):
        return UserModel.query.all()

    def resolve_user(self, info, username):
        return UserModel.query.filter_by(username=username).first()

    def resolve_hello(self, info, name):
        return f"Hello {name}"
