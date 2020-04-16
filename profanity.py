from textblob import TextBlob
from profanity_check import predict, predict_prob


# ro = TextBlob("Toate peste toate smartphone-ul are specificatii de tot, aproape toate componentele fiind high end, "
#               "mai putin display-ul")
# en = TextBlob("Waiting for this laptop and all the rumors were very exciting, but instead Apple has offered us this "
# "piece of shit")
# print(ro.detect_language())
# print(en.detect_language())
# print('Profanity checking: ')
# print(predict(['fu ck it bro']))


def get_profanity(txt, prob=False):
    if not isinstance(txt, str):
        raise Exception('txt has to be a string')
    if len(txt.strip()) == 0:
        return False
    blob = TextBlob(txt)
    lang = blob.detect_language()
    result = None
    # if blob.detect_language() != 'en':
    #   raise Exception('Only english text can be verified for profanity!')
    if lang == 'en':
        if not prob:
            result = bool(predict([txt])[0] == 1)
        else:
            result = predict_prob([txt])[0]
    # aparent egalitatea urmatoarea nu intoarce python bool si trebuie sa convertim la python bool
    return {'result': result, 'lang': lang}
