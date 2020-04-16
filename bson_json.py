# import json
# from bson import ObjectId, BSONDAT
#
#
# class JSONEncoder(json.JSONEncoder):
#     def default(self, o):
#         if isinstance(o, ObjectId):
#             return str(o)
#         return json.JSONEncoder.default(self, o)
from bson import json_util
import json


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        return json.dumps(o, default=json_util.default)
