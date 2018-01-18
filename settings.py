def labels():
    # метки для поиска
    return {
        'Bank': {
            'keywords': 'деньги_NOUN касса_NOUN банк_NOUN заплатить_VERB платежка_NOUN счет_NOUN',
            'form_name': 'ЖурналыДокументов.Деньги.ФормаСписка',
            'element_to_focus': 'None'
        },
        'Trade': {
            'keywords': 'товар_NOUN счет_NOUN продать_NOUN выставлять_VERB торг-12_NOUN',
            'form_name': 'Документы.СчетаНаОплатуПокупателю.Формы.ФормаСписка',
            'element_to_focus': 'None'
        },
        'Performance': {
            'keywords': 'тупит_VERB тормозит_VERB медленно_ADV работает_VERB',
            'form_name': 'Обработки.Производительность.Формы.ФормаОбработки',
            'element_to_focus': 'None'
        },
        'SeparateVATAccounting': {
            'keywords': 'включить_VERB раздельный_ADJ учет_NOUN ндс_NOUN',
            'form_name': 'Обработки.НастройкиНалоговИОтчетов.Формы.ФормаОбработки',
            'element_to_focus': 'РаздельныйУчетНДС'
        }
    }