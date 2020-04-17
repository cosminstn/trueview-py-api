from bson import json_util
import json


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        return json.dumps(o, default=json_util.default)
