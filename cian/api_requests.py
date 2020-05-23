import requests
import xml.etree.ElementTree as ElemTree
from urllib.parse import urlencode
from cian.api_data import CianApiData


def get_metro_stations():
    metro_response = requests.get(CianApiData.METRO_STATIONS_ENDPOINT)
    xml_root = ElemTree.fromstring(metro_response.content)
    metro_stations = {}
    for station in xml_root:
        metro_stations.update({station.text.lower(): station.attrib['id']})
    return metro_stations


def get_result_by_query(query):
    response = requests.get(CianApiData.CIAN_API_ENDPOINT + query)
    return response.content


def get_result_by_query_params(params):
    query = urlencode(params)
    return get_result_by_query(query)
