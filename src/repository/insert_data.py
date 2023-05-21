from src.repository.pymongo_get_database import get_database


def create_collection(collection_name: str):
    dbname = get_database()
    collection_name = dbname[f"{collection_name}"]

    return collection_name
