from pprint import pprint

import pymongo


# https://api.mongodb.com/python/current/tutorial.html

class MongoEngine:
    __instance = None

    _client = None
    _db = None

    @staticmethod
    def get_instance():
        """Static access method."""
        if MongoEngine.__instance is None:
            MongoEngine()
        return MongoEngine.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if MongoEngine.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            MongoEngine.__instance = self
            MongoEngine._client = pymongo.MongoClient("mongodb+srv://cosmin:G83$RyVMQeSHH2@europecluster-ofy68"
                                                      ".mongodb.net/test")
            MongoEngine._db = MongoEngine._client.dev

    def get_server_info(self):
        return self._client.server_info()

    def get_reviews(self):
        reviews = []
        for rev in self._db.Reviews.find({}):
            reviews.append(rev)
        return reviews

    def get_relevant_reviews(self, upc):
        """
        For calculating a products score we cannot use all reviews.
        We must use the reviews for that product, and for the other products in that category.
        Products and Reviews have the UniversalProductCode field stored as EAN-13 (13 digits).
        """

        if len(upc) == 12:
            upc = "0" + upc.strip()

        match_pipeline = {"$match": {
            "UniversalProductCode": upc
        }}

        product = self._db.Products.find_one({"UniversalProductCode": upc})
        if product is not None:
            pprint(product)
            match_pipeline = {"$match": {
                "$or": [
                    {
                        "UniversalProductCode": upc
                    },
                    {
                        "product.Category.ID": product['Category']['ID']
                    }
                ]
            }}

        reviews = self._db.Reviews.aggregate([
            {
                "$lookup": {
                    'from': 'Products',
                    'localField': 'UniversalProductCode',
                    'foreignField': 'UniversalProductCode',
                    'as': 'product'
                }
            },
            {
                '$unwind': {
                    'path': '$product',
                    'preserveNullAndEmptyArrays': True
                }
            },
            match_pipeline,
            {
                '$project': {
                    'Score': 1,
                    'UniversalProductCode': 1,
                    '_id': 0
                }
            }
        ])
        print('Before converting to list: ')
        pprint(reviews)
        return list(reviews)

    def get_all_reviews(self):
        cursor = self._db.Reviews.find({})
        return list(cursor)
