# Mutations means write operations on an object
from graphene import Mutation, String, Field, ObjectType, ID

from db_models import UserModel
from main import db
from schema import User


# Mutation for user
class CreateUser(Mutation):
    class Arguments:
        username = String(required=True)
        fname = String(required=False)
        lname = String(required=False)
        email = String(required=False)
        password = String(required=False)

    user = Field(lambda: User)

    def mutate(self, info, username, email=None, fname=None, lname=None, password=None):
        # Create new user instance
        new_user = UserModel(username=username, email=email, fname=fname, lname=lname)
        if password:
            new_user.set_password(password)
        db.session.add(new_user)

        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise Exception(f"Error creating user: {str(e)}")
        return CreateUser(user=new_user)


class UpdateUser(Mutation):
    class Arguments:
        id = ID(required=True)
        username = String(required=False)
        fname = String(required=False)
        lname = String(required=False)
        email = String(required=False)
        password = String(required=False)

    user = Field(lambda: User)

    def mutate(self, info, **kwargs):

        if "id" in kwargs.keys():
            id = kwargs["id"]
            # Create new user instance
            user = UserModel.query.get(id)
            if not user:
                raise Exception(f"User {id} does not exist")
        else:
            raise Exception(f"Error updating user: ID not provided")

        for key, val in kwargs.items():
            setattr(user, key, val)
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise Exception(f"Error updating user: {str(e)}")
        return UpdateUser(user=user)


# Registering all mutations
class Mutation(ObjectType):
    create_user = CreateUser.Field()
    update_user = UpdateUser.Field()

