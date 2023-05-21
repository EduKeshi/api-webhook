import bcrypt
from flask_jwt_extended import create_access_token

from src.repository.pymongo_get_database import get_database


def login_user_service(request: dict):
    database = get_database()

    collection = database["user"]

    if collection.count_documents({"email": request["email"]}) == 0:
        return False

    users = collection.find(
        {"email": request["email"]}
    )

    if users[0]["email"] == request["email"]:
        if bcrypt.checkpw(request["senha"].encode("utf-8"), users[0]["password"]):
            return create_access_token(identity=request["email"])
    else:
        return False
