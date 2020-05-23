from config.application_config import ApplicationConfig
from cian.api_data import CianApiData
from cian.api_requests import get_result_by_query_params
from cian.metro_params import MetroParams
from cian.query_params import *
from launchers.common import process_result


def get_params_from_config(config):
    region_param = get_region_param()
    metro_params = MetroParams.get_metro_with_radius(
        metro_names=config.get_metro_names(),
        radius=config.get_metro_radius(),
        is_foot_only=config.get_metro_only_foot()
    )

    rooms_params = get_rooms_params(config.get_rooms_number())
    price_params = get_price_params(min_price=config.get_min_price(), max_price=config.get_max_price())
    rent_duration = get_rent_duration(config.get_rent_months_duration())
    publication_time = get_publication_time(config.get_published_hours())

    return {
        **CianApiData.DEFAULT_FLAT_PARAMS,
        **region_param,
        **metro_params,
        **rooms_params,
        **price_params,
        **rent_duration,
        **publication_time
    }


def start_app_with_config(config_file, excel_format):
    config = ApplicationConfig(config_file)
    query_params = get_params_from_config(config)
    result = get_result_by_query_params(query_params)
    process_result(result, excel_format)
