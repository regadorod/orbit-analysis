import re
import pytest

# local libraries
import datahandle as dh

@pytest.fixture
def date_time_input():
     string = "17:05:2000:08:11:45"
     dictLabels = ['D', 'M', 'Y', 'h', 'm', 's']

     return string, dictLabels

def test_string_to_dict(date_time_input):

    dict = dh.string_to_dict(date_time_input[0], date_time_input[1])

    assert dict == {'D':17, 'M': 5, 'Y': 2000, 'h': 8, 'm': 11, 's': 45}