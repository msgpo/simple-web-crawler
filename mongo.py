from pymongo import MongoClient

client = MongoClient('mongodb://root:strong-password@mongodb:27017/')

def save_links(base_url, data, db_name='crawler', collection_name='urls'):
    db = client[db_name]
    collection = db[collection_name]
    document = collection.update(
        {'base_url': base_url},
        {'$set': data},
        True
    )
    return document


def get_base(base_url=None, db_name='crawler', collection_name='urls'):
    documents = collection.find(base_url, {'base_url': 1})
    return list(documents)

