from ...drivers.html_collector import HtmlCollector
from ...drivers.http_requester import HttpRequester
from ..contracts.extract_contract import ExtractContract

from .extract_html import ExtractHtml


def test_extract():
    http_requester = HttpRequester("https://web.archive.org/web/20121007172955/http://www.nga.gov/collection/anZ1.htm")
    html_collector = HtmlCollector()

    extract_html = ExtractHtml(http_requester, html_collector)
    response = extract_html.extract()
    print()
    assert isinstance(response, ExtractContract)

def test_extract_error():
    http_requester = HttpRequester("https://web.archive.org/web/20121007172955/http://www.nga.gov/collection/anZ1.htm")
    html_collector = HtmlCollector()

    extract_html = ExtractHtml(http_requester, html_collector)
    response = extract_html.extract()
    print()
    assert isinstance(response, ExtractContract)
