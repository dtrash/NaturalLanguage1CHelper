from flask import Flask, jsonify, request

import semantic_engine as semantic_engine
from settings import labels

model = semantic_engine.load_w2v_model()
app = Flask(__name__)


@app.route('/GetHelp', methods=['POST'])
def get_help():
    users_query = request.json['query']
    normalized_query = semantic_engine.canonize_words(users_query.split())
    min_distance = 100
    closest_label = ''
    all_labels = labels()
    for label in all_labels:
        normalized_label = semantic_engine.canonize_words(all_labels[label]['keywords'].split())
        label_distance = model.wmdistance(normalized_query, normalized_label)
        if label_distance < min_distance:
            min_distance = label_distance
            closest_label = label

    return jsonify({
        'answer': closest_label,
        'normalized_user_query': normalized_query,
        'form': all_labels[closest_label]['form_name']
    })


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
    app.config['JSON_AS_ASCII'] = False
    app.run(host='martyshin-s', debug=True)