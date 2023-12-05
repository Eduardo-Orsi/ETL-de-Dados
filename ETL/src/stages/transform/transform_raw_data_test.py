#pylint: disable=unused-variable
#pylint: disable=broad-exception-caught

from .transform_raw_data import TransformRawData
from ..contracts.mocks.extract_contract import extract_contract_mock
from ..contracts.transform_contract import TransformContract
from ...errors.transform_error import TransformError

def test_transform():
    transform_raw_data = TransformRawData()
    transformed_information = transform_raw_data.transform(extract_contract_mock)
    print(transformed_information)
    assert isinstance(transformed_information, TransformContract)
    assert isinstance(transformed_information.load_content, list)
    assert isinstance(transformed_information.load_content[0], dict)
    assert 'first_name' in transformed_information.load_content[0]
    assert 'second_name' in transformed_information.load_content[0]
    assert 'surname' in transformed_information.load_content[0]
    assert 'artist_id' in transformed_information.load_content[0]
    assert 'link' in transformed_information.load_content[0]
    assert 'extraction_date' in transformed_information.load_content[0]

def test_transform_error():
    transform_raw_data = TransformRawData()
    try:
        transformed_information = transform_raw_data.transform('entrada com erro')
    except Exception as exception:
        assert isinstance(exception, TransformError)
