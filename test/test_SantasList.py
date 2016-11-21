# test_santaslist.py

import yaml
import santaslist
import pytest

TEST_PEOPLE_STR = 'jeff hann (@obihann),bob bober (@bob),frank franklyn (@franky),george the dog (@george)'


@pytest.fixture()
def load_people():
    data = open('test/people.yml', 'r')
    return santaslist.load_people(yaml.load(data)['people'])


class TestSantasList(object):
    def test_load_people(self, load_people):
        assert isinstance(load_people.people, santaslist.People)

    def test_list_people(self, load_people):
        assert TEST_PEOPLE_STR == str(santaslist.list_people())
        assert isinstance(santaslist.list_people(), santaslist.People)

    def test_list_matches(self, load_people):
        assert isinstance(santaslist.matches(), santaslist.Pairs)
        assert str(santaslist.matches()) != ''
