import pandas


DEFAULT_FIELDS_TO_EXTRACT = [
    'Метро',
    'Площадь, м2',
    'Дом',
    'Цена',
    'Телефоны',
    'Описание',
    'Ремонт',
    'Ссылка на объявление'
]


def parse_cian_data(data, fields_to_extract=DEFAULT_FIELDS_TO_EXTRACT):
    readed = pandas.read_excel(data)
    return readed.loc[:, fields_to_extract]

