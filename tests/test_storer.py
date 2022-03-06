import pytest
import os
import re

from project0 import storer, parser


@pytest.fixture
def sample_incidents():
    return [
        parser.Incident('2/24/2022 1:05',
                        '2022-00010284',
                        '1306 168TH AVE NE',
                        '911 Call Nature Unknown',
                        'OK0140200'),
        parser.Incident('2/24/2022 8:20',
                        '2022-00003471',
                        '',
                        '',
                        'EMSSTAT')
    ]


@pytest.fixture(scope='module')
def db():
    test_db_file = 'test_normanpd.db'

    # Setup
    db = storer.create_db(test_db_file)
    yield db

    # Teardown
    if os.path.exists(test_db_file):
        os.remove(test_db_file)


def test_create_db_should_return_connectable_db(db):
    assert db.check_con()


def test_get_stats_should_return_formatted_natures_count_string(
        db, sample_incidents):
    inserted_count = db.add_incidents(sample_incidents)
    assert inserted_count == len(sample_incidents)

    got = db.get_stats()
    want = '911 Call Nature Unknown|1'
    assert re.search(want, got) is not None
