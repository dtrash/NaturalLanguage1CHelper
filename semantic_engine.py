import gensim
import pymorphy2
from nltk.corpus import stopwords

from settings import path_to_corpora


def load_w2v_model():
    w2v_model = gensim.models.KeyedVectors.load_word2vec_format(path_to_corpora(), encoding='utf-8')
    print('word2vec model with ruwikiruscorpora loaded')
    return w2v_model


# http://textmechanic.com/text-tools/basic-text-tools/remove-duplicate-lines/
# http://www.codeisart.ru/blog/python-shingles-algorithm/
def canonize_words(words: list) -> list:

    # поиск нормальной формы слова и добавление тега определяющего часть речи

    grammar_map = {
        'NOUN': '_NOUN',
        'VERB': '_VERB', 'INFN': '_VERB', 'GRND': '_VERB', 'PRTF': '_VERB', 'PRTS': '_VERB',
        'ADJF': '_ADJ', 'ADJS': '_ADJ',
        'ADVB': '_ADV',
        'PRED': '_ADP'
    }

    stop_words = stopwords.words('russian')

    normalized = []
    morph_analyzer = pymorphy2.MorphAnalyzer()

    for w in words:
        forms = morph_analyzer.parse(w.lower())
        try:
            form = max(forms, key=lambda x: (x.score, x.methods_stack[0][2]))
        # Нужно посмотреть какие исключения библиотеки здесь могут быть
        except Exception:
            form = forms[0]
            print(form)
        if not (form.tag.POS in ['PREP', 'CONJ', 'PRCL', 'NPRO', 'NUMR']
                or 'Name' in form.tag
                or 'UNKN' in form.tag
                or form.normal_form in stop_words):  # 'ADJF'
            norm_word = form.normal_form.replace("ё", "е")
            normalized.append(norm_word + grammar_map.get(form.tag.POS, ''))
    return normalized
