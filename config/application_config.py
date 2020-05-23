import configparser
from cian.api_data import CianApiData


class ApplicationConfig:
    def __init__(self, config_path):
        config = configparser.ConfigParser()
        config.read([config_path], 'utf-8')
        self.config = config

    def __get_int_or_none(self, section, key):
        return self.config.getint(section, key, fallback=None)

    def __get_splitted_params(self, section, key):
        objects = self.config.get(section, key, fallback=None)
        if objects:
            objects = objects.split(',')
        return objects

    # metro stations
    def get_metro_names(self):
        return self.__get_splitted_params('metro', 'stations')

    def get_metro_radius(self):
        return self.__get_int_or_none('metro', 'radius')

    def get_metro_only_foot(self):
        return self.config.getboolean('metro', 'only_foot', fallback=None)

    # rooms
    @staticmethod
    def __get_room_as_number(room):
        if room.lower() == 'studio':
            return CianApiData.STUDIO
        if room.lower() == 'open_plan':
            return CianApiData.OPEN_PLAN
        return int(room)

    def get_rooms_number(self):
        rooms = self.__get_splitted_params('rooms', 'number')
        rooms_numbers = list(map(ApplicationConfig.__get_room_as_number, rooms))
        if rooms_numbers:
            return list(filter(lambda x: x in CianApiData.VALID_ROOMS_NUMBERS, rooms_numbers))
        return rooms_numbers

    # prices
    def get_min_price(self):
        return self.__get_int_or_none('prices', 'min_price')

    def get_max_price(self):
        return self.__get_int_or_none('prices', 'max_price')

    # duration
    def get_rent_months_duration(self):
        return self.__get_int_or_none('duration', 'months')

    # publication time
    def get_published_hours(self):
        return self.__get_int_or_none('published', 'hours')
