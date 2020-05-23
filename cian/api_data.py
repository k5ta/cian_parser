class CianApiData:
    CIAN_API_ENDPOINT = 'https://www.cian.ru/export/xls/offers/?'
    METRO_STATIONS_ENDPOINT = 'https://www.cian.ru/metros-moscow.xml'

    DEFAULT_FLAT_PARAMS = {
        'engine_version': 2,
        'currency': 2,
        'deal_type': 'rent',
        'offer_type': 'flat'
    }

    # rooms number
    OPEN_PLAN = 7
    STUDIO = 9
    VALID_ROOMS_NUMBERS = [*(range(1, OPEN_PLAN)), OPEN_PLAN, STUDIO]
