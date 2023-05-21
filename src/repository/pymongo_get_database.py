from pymongo import MongoClient


def get_database():
    connection_string = "mongodb://localhost:27017"

    client = MongoClient(connection_string)

    return client['user_status']


if __name__ == "__main__":
    dbname = get_database()
