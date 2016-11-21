from santaslist.objects import People
from santaslist.objects import Pairs


class SantasList(object):
    def __init__(self, people: list) -> None:
        """
        Initialize a list of people

        :param people:
        :rtype: None
        """
        self._people = People(people)
        self._pairs = Pairs(self._people)

    @property
    def people(self) -> People:
        """
        Return all people participating

        :rtype: People
        """
        return self._people

    @property
    def matches(self) -> Pairs:
        """
        Return the matched people

        :rtype: Pairs
        """
        return self._pairs
