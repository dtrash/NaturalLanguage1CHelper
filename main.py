# from flask import Flask, jsonify

import semantic_engine as semantic_engine
from settings import labels


# app = Flask(__name__)


# @app.route('/GetHelp')
def get_help():
    query_bank = 'программа медленно работает'.split()
    normalized_query = semantic_engine.canonize_words(query_bank)
    min_distance = 100
    closest_label = ''
    all_labels = labels()
    for label in all_labels:
        label_distance = model.wmdistance(normalized_query, all_labels[label]['keywords'].split())
        if label_distance < min_distance:
            min_distance = label_distance
            closest_label = label

    # return jsonify({'answer': closest_label})
    return closest_label


if __name__ == '__main__':
    """
    before start need to download corpora from link below  to /data folder 
    http://rusvectores.org/static/models/rusvectores4/ruwikiruscorpora/ruwikiruscorpora_upos_skipgram_300_2_2018.vec.gz

    must have libraries: (pip install 'library_name')
        * flask
        * gensim
        * pymorphy2
        * nltk - with stopwords
    """
    model = semantic_engine.load_w2v_model()
    print(get_help())
    # app.run(debug=True)