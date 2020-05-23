from cian.api_requests import get_metro_stations


class MetroParams:
    stations = get_metro_stations()

    @staticmethod
    def get_metro_with_radius(metro_names, radius=None, is_foot_only=False):
        metro_data = {}
        for i in range(len(metro_names)):
            name = metro_names[i].lower()
            station_key = 'metro[%s]' % i
            metro_data.update({station_key: MetroParams.stations[name]})
        if radius:
            metro_data.update({'foot_min': radius})
            only_foot = 2 if is_foot_only else -2
            metro_data.update({'only_foot': only_foot})
        return metro_data
