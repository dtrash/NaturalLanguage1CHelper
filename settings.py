def labels():
    # метки для поиска
    return {
        'Bank': {
            'keywords': 'заплатить оплатить оплата деньги касса банк платежка счет',
            'form_name': 'ЖурналДокументов.Деньги.ФормаСписка',
            'element_to_focus': 'None'
        },
        'Trade': {
            'keywords': 'товар счет продать выставлять торг-12',
            'form_name': 'Документ.СчетНаОплатуПокупателю.ФормаСписка',
            'element_to_focus': 'None'
        },
        'Performance': {
            'keywords': 'тупить тормозить медленно работать',
            'form_name': 'Обработка.ПанельАдминистрированияБП.Форма.Производительность',
            'element_to_focus': 'None'
        },
        'SeparateVATAccounting': {
            'keywords': 'включить раздельный учет ндс',
            'form_name': 'ОбщаяФорма.НалогиИОтчеты',
            'element_to_focus': 'РаздельныйУчетНДС'
        }
    }


def path_to_corpora():
    return r'C:\Users\martyshin_s\PycharmProjects\NaturalLanguage1CHelper\ruwikiruscorpora_upos_skipgram_300_2_2018.vec.gz'