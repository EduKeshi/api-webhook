import bcrypt

from src.repository.insert_data import create_collection
from src.repository.pymongo_get_database import get_database


def create_user_service(request: dict):
    get_database()
    user_collection = create_collection("user")

    if request["token"] != "uhdfaAADF123":
        return {"invalid_token": "Token inválido"}

    salt = bcrypt.gensalt()

    new_user = {
        "email": request["email"],
        "password": bcrypt.hashpw(request["senha"].encode("utf-8"), salt)
    }

    user_collection.insert_one(new_user)
