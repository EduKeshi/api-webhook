from src.repository.pymongo_get_database import get_database


def attempts_service(email: str):
    database = get_database()

    collection = database["attempts"]

    attempts = collection.find(
        {"email": email})

    attempts_list = list()

    for attempt in attempts:
        attempts_list.append({
            "email": attempt["email"],
            "status": attempt["status"],
            "payload": attempt["payload"]
        })

    return attempts_list
