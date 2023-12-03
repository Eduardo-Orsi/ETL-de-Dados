from .transform_raw_data import TransformRawData
from ..contracts.mocks.extract_contract import extract_contract_mock

def test_transform():
    transform_raw_data = TransformRawData()
    transformed_information = transform_raw_data.transform(extract_contract_mock)
    assert isinstance(transformed_information, list)
    assert isinstance(transformed_information[0], dict)
    assert 'first_name' in transformed_information[0]
    assert 'second_name' in transformed_information[0]
    assert 'surname' in transformed_information[0]
    assert 'artist_id' in transformed_information[0]
    assert 'link' in transformed_information[0]
    assert 'extraction_date' in transformed_information[0]
