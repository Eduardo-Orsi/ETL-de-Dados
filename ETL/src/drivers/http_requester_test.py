from .http_requester import HttpRequester

def test_request_from_page(requests_mock):
    response_context = "<h1>Teste Titulo</h1>"
    requests_mock.get("https://google.com.br", status_code=200, text=response_context)
    http_requester = HttpRequester("https://google.com.br")
    request_response = http_requester.request_from_page()
    print(request_response)

    assert 'status_code' in request_response
    assert 'html'in request_response
    assert request_response["status_code"] == 200
    assert request_response["html"] == response_context
