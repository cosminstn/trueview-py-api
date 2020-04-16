from flask import Flask, request, jsonify, Response

import profanity
from bson_json import JSONEncoder
from mongo import MongoEngine
from stars import Ratings

app = Flask(__name__)


@app.route('/profanity/decide', methods=['POST'])
def is_profanity():
    # if request.content_type != 'application/json':
    #     raise BadRequest('Content-Type has to be application/json')
    app.logger.info('getting profanity decide')
    print('getting profanity decide')
    req = request.get_json()
    txt = req.get('txt')
    return jsonify(profanity.get_profanity(txt))


@app.route('/profanity/prob', methods=['POST'])
def prob():
    # if request.content_type != 'application/json':
    #     raise BadRequest('Content-Type has to be application/json')
    req = request.get_json()
    txt = req.get('txt')
    return jsonify(profanity.get_profanity(txt, prob=True))


# @app.route('/info', methods=['GET'])
# def get_status():
#     return jsonify({'db': MongoEngine.get_instance().get_server_info()})

#
# @app.route('/reviews', methods=['GET'])
# def get_all_reviews():
#     return JSONEncoder().encode(MongoEngine.get_instance().get_reviews())


@app.route("/scores", methods=['GET'])
def get_scores():
    data_frame = MongoEngine.get_instance().get_reviews_data_frame()
    ratings = Ratings(data=data_frame, prior=3.25, confidence=7)
    print('Describe')
    print(ratings.describe())
    return Response(response=ratings.get_scores().to_json(),
                    status=200,
                    mimetype='application/json')


@app.route("/scores/bayes/<upc>", methods=['GET'])
def get_bayes_product_score(upc):
    """
    :param upc The universal product code, most likely to be an EAN13 code.
    """
    data_frame = MongoEngine.get_instance().get_reviews_data_frame()
    prior = 3.25
    confidence = 7
    ratings = Ratings(data=data_frame, prior=prior, confidence=confidence)
    product_score = ratings.get_product_score(upc)
    response = {
        "bayes": product_score,
        "prior": prior,
        "confidence": confidence
    }
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
