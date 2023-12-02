from typing import Dict
import requests
from .interfaces.http_requester import HttpRequesterInterface


class HttpRequester(HttpRequesterInterface):

    def __init__(self, url: str) -> None:
        self.__url = url

    def request_from_page(self) -> Dict[int, str]:
        response = requests.get(self.__url, timeout=None)
        return {
            "status_code": response.status_code,
            "html": response.text
        }
