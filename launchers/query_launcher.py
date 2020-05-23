from cian.api_requests import get_result_by_query
from launchers.common import process_result


def start_app_with_query(query, excel_format):
    result = get_result_by_query(query)
    process_result(result, excel_format)
