# Mutations means write operations on an object
from datetime import datetime

from graphene import Mutation, String, Field, ObjectType, ID, Boolean

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

        if "username" in kwargs.keys():
            username = kwargs["username"]
            # Create new user instance
            user = UserModel.query.get(username=username)
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


class SoftDeleteUser(Mutation):
    class Arguments:
        username = String(required=True)

    # Response
    success = Boolean()
    message = String(required=True)

    def mutate(self, info, username):
        try:
            user = UserModel.query.get(username=username)
            if not user:
                return SoftDeleteUser(success=False, message=f"User {id} does not exist")
            if not user.is_active:
                return SoftDeleteUser(success=False, message=f"User {id} is not an active user.")

            user.is_active = False
            user.updated_at = datetime.utcnow()
            #Save changes
            db.session.commit()
            return SoftDeleteUser(success=True, message=f"User {id} has been deleted.")

        except Exception as e:
            db.session.rollback()
            return HardDeleteUser(success=False, message=f"Error while deleting user: {str(e)}")


class HardDeleteUser(Mutation):
    class Arguments:
        username = String(required=True, description="Username to be permanently deleted")

    # Response
    success = Boolean()
    message = String(required=True)

    def mutate(self, info, username):
        try:
            user = UserModel.query.get(username=username)
            if not user:
                return HardDeleteUser(success=False, message=f"User {id} does not exist")

            # Save
            db.session.delete(user)
            db.session.commit()
            return HardDeleteUser(success=True, message=f"User {id} has been deleted permanently")
        except Exception as e:
            db.session.rollback()
            return HardDeleteUser(success=False, message=f"Error while deleting user: {str(e)}")
# Registering all mutations
class Mutation(ObjectType):
    create_user = CreateUser.Field()
    update_user = UpdateUser.Field()
    soft_delete_user = SoftDeleteUser.Field()
    hard_delete_user = HardDeleteUser.Field()

