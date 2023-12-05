#pylint: disable=line-too-long
import datetime
from ...contracts.transform_contract import TransformContract

transform_contract_mock = TransformContract (
    load_content=[
        {'first_name': 'Anton Maria', 'second_name': 'Zanetti', 'surname': None, 'artist_id': '11133', 'link': 'https://web.archive.org/web/20121007172955/http://www.nga.gov/cgi-bin/tsearch?artistid=11133', 'extraction_date': datetime.date(2023, 12, 4)},
        {'first_name': 'Leopoldina', 'second_name': 'Zanetti Borzino', 'surname': None, 'artist_id': '3455', 'link': 'https://web.archive.org/web/20121007172955/http://www.nga.gov/cgi-bin/tsearch?artistid=3455', 'extraction_date': datetime.date(2023, 12, 4)},
        {'first_name': 'conte', 'second_name': 'Zanetti I', 'surname': 'Antonio Maria', 'artist_id': '3454', 'link': 'https://web.archive.org/web/20121007172955/http://www.nga.gov/cgi-bin/tsearch?artistid=3454', 'extraction_date': datetime.date(2023, 12, 4)},
        {'first_name': 'Jacopo', 'second_name': 'Zanguidi', 'surname': None, 'artist_id': '961', 'link': 'https://web.archive.org/web/20121007172955/http://www.nga.gov/cgi-bin/tsearch?artistid=961', 'extraction_date': datetime.date(2023, 12, 4)},
        {'first_name': 'Giuseppe', 'second_name': 'Zanini', 'surname': None, 'artist_id': '11597', 'link': 'https://web.archive.org/web/20121007172955/http://www.nga.gov/cgi-bin/tsearch?artistid=11597', 'extraction_date': datetime.date(2023, 12, 4)},
        {'first_name': 'Giuseppe', 'second_name': 'Zanini-Viola', 'surname': None, 'artist_id': '11597', 'link': 'https://web.archive.org/web/20121007172955/http://www.nga.gov/cgi-bin/tsearch?artistid=11597', 'extraction_date': datetime.date(2023, 12, 4)},
        {'first_name': 'Giampietro', 'second_name': 'Zanotti', 'surname': None, 'artist_id': '11631', 'link': 'https://web.archive.org/web/20121007172955/http://www.nga.gov/cgi-bin/tsearch?artistid=11631', 'extraction_date': datetime.date(2023, 12, 4)},
        {'first_name': 'Wou-Ki', 'second_name': 'Zao', 'surname': None, 'artist_id': '3427', 'link': 'https://web.archive.org/web/20121007172955/http://www.nga.gov/cgi-bin/tsearch?artistid=3427', 'extraction_date': datetime.date(2023, 12, 4)}
    ]
)
