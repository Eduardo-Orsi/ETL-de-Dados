#pylint: disable=line-too-long
from datetime import date
from ..extract_contract import ExtractContract


extract_contract_mock = ExtractContract(
    raw_information_content=[
        {'name': 'Zanetti, Anton Maria', 'link': 'https://web.archive.org/web/20121007172955/http://www.nga.gov/cgi-bin/tsearch?artistid=11133'},
        {'name': 'Zanetti Borzino, Leopoldina', 'link': 'https://web.archive.org/web/20121007172955/http://www.nga.gov/cgi-bin/tsearch?artistid=3455'},
        {'name': 'Zanetti I, Antonio Maria, conte', 'link': 'https://web.archive.org/web/20121007172955/http://www.nga.gov/cgi-bin/tsearch?artistid=3454'},
        {'name': 'Zanguidi, Jacopo', 'link': 'https://web.archive.org/web/20121007172955/http://www.nga.gov/cgi-bin/tsearch?artistid=961'},
        {'name': 'Zanini, Giuseppe', 'link': 'https://web.archive.org/web/20121007172955/http://www.nga.gov/cgi-bin/tsearch?artistid=11597'},
        {'name': 'Zanini-Viola, Giuseppe', 'link': 'https://web.archive.org/web/20121007172955/http://www.nga.gov/cgi-bin/tsearch?artistid=11597'},
        {'name': 'Zanotti, Giampietro', 'link': 'https://web.archive.org/web/20121007172955/http://www.nga.gov/cgi-bin/tsearch?artistid=11631'},
        {'name': 'Zao Wou-Ki', 'link': 'https://web.archive.org/web/20121007172955/http://www.nga.gov/cgi-bin/tsearch?artistid=3427'},
        {'name': 'Zas-Zie', 'link': 'https://web.archive.org/web/20121007172955/http://www.nga.gov/collection/anZ2.htm'},
        {'name': 'Zie-Zor', 'link': 'https://web.archive.org/web/20121007172955/http://www.nga.gov/collection/anZ3.htm'},
        {'name': '<strong>next<br/>page</strong>', 'link': 'https://web.archive.org/web/20121007172955/http://www.nga.gov/collection/anZ4.htm'}
    ],
    extraction_date=date.today()
)
