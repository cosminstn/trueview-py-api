import pymongo
import pandas as pd


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

    def get_reviews_data_frame(self):
        cursor = self._db.Reviews.find({})
        df = pd.DataFrame(list(cursor))

        return df
