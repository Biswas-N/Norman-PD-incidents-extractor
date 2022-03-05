import pytest
from project0 import parser


@pytest.fixture
def sample_unparsed_incidents():
    return [('2/24/2022 1:05',
             '2022-00010284',
             '1306 168TH AVE NE',
             '911 Call Nature Unknown',
             'OK0140200'),
            ('2/24/2022 1:14',
             '2022-00003461',
             '700 S TELEPHONE RD',
             'Transfer/Interfacility',
             'EMSSTAT'),
            ('2/24/2022 2:09',
             '2022-00010285',
             '2320 W MAIN ST',
             'Welfare Check',
             'OK0140200'),
            ('2/24/2022 2:31',
             '2022-00010286',
             'CHAUTAUQUA AVE / W STATE HWY 9 HWY',
             'Traffic Stop',
             'OK0140200'),
            ('2/24/2022 8:20', '2022-00003471', '', '', 'EMSSTAT'),
            ('2/24/2022 18:01', '2022-00003507', '', '', 'EMSSTAT')]


def test_extract_incidents_should_return_a_list(
        sample_unparsed_incidents):
    got = parser.extract_incidents(sample_unparsed_incidents)
    want = [
        parser.Incident(
            sample_unparsed_incidents[0][0],
            sample_unparsed_incidents[0][1],
            sample_unparsed_incidents[0][2],
            sample_unparsed_incidents[0][3],
            sample_unparsed_incidents[0][4]),
        parser.Incident(
            sample_unparsed_incidents[1][0],
            sample_unparsed_incidents[1][1],
            sample_unparsed_incidents[1][2],
            sample_unparsed_incidents[1][3],
            sample_unparsed_incidents[1][4]),
        parser.Incident(
            sample_unparsed_incidents[2][0],
            sample_unparsed_incidents[2][1],
            sample_unparsed_incidents[2][2],
            sample_unparsed_incidents[2][3],
            sample_unparsed_incidents[2][4]),
        parser.Incident(
            sample_unparsed_incidents[3][0],
            sample_unparsed_incidents[3][1],
            sample_unparsed_incidents[3][2],
            sample_unparsed_incidents[3][3],
            sample_unparsed_incidents[3][4]),
        parser.Incident(
            sample_unparsed_incidents[4][0],
            sample_unparsed_incidents[4][1],
            sample_unparsed_incidents[4][2],
            sample_unparsed_incidents[4][3],
            sample_unparsed_incidents[4][4]),
        parser.Incident(
            sample_unparsed_incidents[5][0],
            sample_unparsed_incidents[5][1],
            sample_unparsed_incidents[5][2],
            sample_unparsed_incidents[5][3],
            sample_unparsed_incidents[5][4]),
    ]

    assert len(got) == 6
    assert got == want
