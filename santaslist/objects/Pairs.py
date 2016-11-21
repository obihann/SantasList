import random

from santaslist.objects import People
from santaslist.objects import Person


class Pair(tuple):
    def __new__(self, a: Person, b: Person) -> tuple:
        """
        Group two people

        :param a:
        :param b:
        """
        assert isinstance(a, Person) and isinstance(b, Person)
        return tuple.__new__(Pair, (a, b))

    def __str__(self) -> str:
        """
        Display both people joined together for the first time

        :rtype: str
        """
        return '%s <---> %s' % (self[0], self[1])


class Pairs(list):
    _pairs = []

    def __init__(self, people: People) -> None:
        """
        Load a list of People and pair them

        :param people:
        :rtype: None
        """
        assert isinstance(people, People)

        while len(people) > 0:
            a = self._pop_list(people)
            b = self._pop_list(people)

            self._pairs.append(Pair(a, b))

        list.__init__(self, self._pairs)

    def __str__(self) -> str:
        """
        Return all pairs in a string

        :rtype: str
        """
        return '\n'.join(str(x) for x in self._pairs)

    @staticmethod
    def _pop_list(my_list: People) -> Person:
        """
        Take a list of People and remove a random choice, then remove that Person

        :param my_list:
        :rtype: Person
        """
        assert isinstance(my_list, People)
        indices = list(range(0, len(my_list)))

        x = random.choice(indices)
        y = my_list[x]

        del indices[x]
        del my_list[x]

        return y
