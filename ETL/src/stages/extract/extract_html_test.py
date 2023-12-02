from ...drivers.tests.http_requester import HttpRequesterSpy
from ...drivers.tests.html_collector import HtmlCollectorSpy
from ..contracts.extract_contract import ExtractContract

from .extract_html import ExtractHtml


def test_extract():
    http_requester = HttpRequesterSpy()
    html_collector = HtmlCollectorSpy()

    extract_html = ExtractHtml(http_requester, html_collector)
    response = extract_html.extract()
    print()
    print(response)
    assert isinstance(response, ExtractContract)
    assert http_requester.request_from_page_count == 1
    assert 'html' in html_collector.collect_essential_information_attributes

def test_extract_error():
    http_requester = HttpRequesterSpy()
    html_collector = HtmlCollectorSpy()

    extract_html = ExtractHtml(http_requester, html_collector)
    response = extract_html.extract()
    print()
    assert isinstance(response, ExtractContract)
