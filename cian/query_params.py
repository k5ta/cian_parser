def get_region_param(region_id=1):  # default id for msk
    return {'region': region_id}


def get_rooms_params(rooms_numbers):
    if not rooms_numbers:
        rooms_numbers = []
    rooms = list(map(lambda x: ('room%s' % x, 1), rooms_numbers))
    return dict(rooms)


def get_price_params(min_price, max_price):
    if not min_price:
        min_price = 0
    if not max_price:
        max_price = 0

    if min_price > max_price:
        raise Exception("Wrong params: min_price is greater than max_price: %s > %s" % (min_price, max_price))
    all_prices = {}

    if min_price > 0:
        all_prices['min_price'] = min_price
    if max_price > 0:
        all_prices['max_price'] = max_price
    return all_prices


def get_rent_duration(months):
    if not months:
        rent_type = 4
    elif months >= 12:
        rent_type = -2
    elif 0 < months < 12:
        rent_type = 3
    else:
        raise Exception("Wrong rent months param: got %s" % months)
    return {'type': rent_type}


def get_publication_time(hours):
    time = 0
    if hours and hours > 0:
        time = hours * 3600
    return {'totime': time}
