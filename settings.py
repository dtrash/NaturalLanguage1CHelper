def labels():
    # метки для поиска
    return {
        'Bank': {
            'keywords': 'деньги_NOUN касса_NOUN банк_NOUN заплатить_VERB платежка_NOUN счет_NOUN',
            'form_name': 'ЖурналДокументов.Деньги.ФормаСписка',
            'element_to_focus': 'None'
        },
        'Trade': {
            'keywords': 'товар_NOUN счет_NOUN продать_NOUN выставлять_VERB торг-12_NOUN',
            'form_name': 'Документ.СчетНаОплатуПокупателю.ФормаСписка',
            'element_to_focus': 'None'
        },
        'Performance': {
            'keywords': 'тупить_VERB тормозить_VERB медленно_ADV работать_VERB',
            'form_name': 'Обработка.ПанельАдминистрированияБП.Форма.Производительность',
            'element_to_focus': 'None'
        },
        'SeparateVATAccounting': {
            'keywords': 'включить_VERB раздельный_ADJ учет_NOUN ндс_NOUN',
            'form_name': 'ОбщаяФорма.НалогиИОтчеты',
            'element_to_focus': 'РаздельныйУчетНДС'
        }
    }


def path_to_corpora():
    return r'C:\Users\martyshin_s\PycharmProjects\NaturalLanguage1CHelper\ruwikiruscorpora_upos_skipgram_300_2_2018.vec.gz'