from santaslist.objects import Pairs
from santaslist.objects import People
from santaslist.SantasList import SantasList

__author__ = 'Jeffrey Hann'
__version__ = '0.0.7'

_theList = People()


def load_people(people: list) -> People:
    """
    Load a list of people

    :param people:
    :rtype: People
    """
    global _theList
    _theList = SantasList(people)
    return _theList


def list_people() -> People:
    """
    Return all people

    :rtype: People
    """
    global _theList
    return _theList.people


def matches() -> Pairs:
    """
    Return paired people

    :rtype: Pairs
    """
    global _theList
    return _theList.matches
