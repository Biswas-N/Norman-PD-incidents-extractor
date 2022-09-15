from types import NoneType
import io

import pytest
import pandas as pd
from project0 import downloader


def test_fetch_incidents_should_return_unparsed_data_for_valid_url():
    valid_url = 'https://www.normanok.gov/sites/default/files/documents/2022-08/2022-08-01_daily_incident_summary.pdf'
    got = downloader.fetch_incidents(valid_url)

    assert len(got) > 0


def test_fetch_incidents_should_return_nothing_for_invalid_url():
    invalid_url = 'https://www.normanok.gov/blah.pdf'
    got = downloader.fetch_incidents(invalid_url)

    assert isinstance(got, NoneType)


@pytest.fixture
def sample_file():
    with open('./tests/resources/sample.pdf', 'rb') as f:
        return io.BytesIO(f.read())


@pytest.fixture
def sample_file_df():
    return pd.read_csv('./tests/resources/sample_output.csv')


def test_extract_incidents_should_return_data_as_list_for_valid_file(
        sample_file, sample_file_df):
    got = downloader.extract_incidents(sample_file)

    assert len(got) == len(sample_file_df.index)


def test_extract_incidents_should_return_nothing_for_invalid_file():
    got = downloader.extract_incidents(io.BytesIO(b'Not a valid PDF BytesIO'))

    assert isinstance(got, NoneType)
