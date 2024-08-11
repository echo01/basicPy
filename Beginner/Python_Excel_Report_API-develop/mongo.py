from pymongo import MongoClient


def get_database():
    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = "mongodb://root:example@localhost/passport"

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = MongoClient(CONNECTION_STRING, authSource='admin')

    # Create the database for our example (we will use the same database throughout the tutorial
    return client.passport

def get_collection(client, collection_name):
    return client[collection_name]
