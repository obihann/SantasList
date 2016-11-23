# __init__.py
import random


__author__ = 'Jeffrey Hann'
__version__ = '1.0.0'

_people = []
_pairs = []


def _build_pairs(givers: list) -> list:
    """
    Load a list of People and pair them

    :param givers:
    :rtype: None
    """
    random.shuffle(givers)

    new_pairs = [pair for pair in zip(givers, givers[1:])]
    new_pairs.append((givers[-1], givers[0]))

    return new_pairs


def _pop_list(my_list: list) -> dict:
    """
    Take a list of people and remove a random choice

    :param my_list: list
    :rtype: dict
    """
    # pick random person
    x = random.choice(my_list)

    # grab user
    y = my_list[x]

    # remove items from the lists
    del my_list[x]

    return y


def _format_pair(pair: tuple) -> str:
    """
    Print all the pairs

    :param pair: tuple
    :rtype: str
    """
    return '%s ----> %s' % (_format_person(pair[0]), _format_person(pair[1]))


def _format_person(data:dict) -> str:
    """
    Print a person dictionary in a sexy format

    :param data: dict
    :rtype: str
    """
    assert 'name' in data and 'username' in data
    return '%s (%s)' % (data['name'], data['username'])


def load_people(data: list) -> list:
    """
    Load a list of people

    :param data: list
    :rtype: list
    """
    global _people, _pairs
    _people = data
    _pairs = _build_pairs(_people[:])

    return _people


def people() -> list:
    """
    Return all people

    :rtype: list
    """
    return _people


def pairs() -> list:
    """
    return list

    :rtype: list
    """
    return _pairs


def print_people() -> str:
    """
    return a nicely formatted string of people

    :rtype: str
    """
    return ','.join(_format_person(x) for x in _people)


def print_pairs() -> str:
    """
    Return a nice sexy list of all paired people

    :rtype: str
    """
    return '\n'.join(_format_pair(x) for x in _pairs)
