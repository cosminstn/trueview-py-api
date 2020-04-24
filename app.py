from pprint import pprint

from flask import Flask, request, jsonify, Response

import profanity
import pandas as pd
from mongo import MongoEngine
from stars import Ratings

app = Flask(__name__)

PRIOR = 3.5
CONFIDENCE = 7


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


@app.route("/scores", methods=['GET'])
def get_scores():
    data_frame = pd.DataFrame(MongoEngine.get_instance().get_all_reviews())
    ratings = Ratings(data=data_frame, prior=PRIOR, confidence=CONFIDENCE)
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
    reviews = MongoEngine.get_instance().get_relevant_reviews(upc)
    print('Reviews')
    pprint(reviews)
    data_frame = pd.DataFrame(reviews)
    if data_frame.empty:
        return Response(status=404,mimetype='application/json')
    print('Data frame')
    pprint(data_frame)
    ratings = Ratings(data=data_frame, prior=PRIOR, confidence=CONFIDENCE)
    product_score = ratings.get_product_score(upc)
    response = {
        "bayes": product_score,
        "prior": PRIOR,
        "confidence": CONFIDENCE
    }
    print('determined score: ' + product_score.__str__() + ' for upc: ' + upc)
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
