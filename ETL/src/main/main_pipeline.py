from ..stages.extract.extract_html import ExtractHtml
from ..stages.transform.transform_raw_data import TransformRawData
from ..stages.load.load_data import LoadData
from ..drivers.http_requester import HttpRequester
from ..drivers.html_collector import HtmlCollector
from ..infra.database import DatabaseConnector
from ..infra.database_repository import DatabaseRepository


class MainPipeline:

    def __init__(self) -> None:
        self.__http_requester = HttpRequester(
            "https://web.archive.org/web/20121007172955/http://www.nga.gov/collection/anZ1.htm"
        )
        self.__extract_html = ExtractHtml(self.__http_requester, HtmlCollector())
        self.__transform_raw_data = TransformRawData()
        self.__load_data = LoadData(DatabaseRepository())

    def run_pipeline(self) -> None:
        DatabaseConnector.connect()
        extract_contract = self.__extract_html.extract()
        transformed_data_contract = self.__transform_raw_data.transform(extract_contract)
        self.__load_data.load(transformed_data_contract)
