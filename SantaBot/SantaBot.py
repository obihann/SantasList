from SantaBot.Objects import People
from SantaBot.Objects import Pairs


class SantaBot(object):
    def __init__(self, people):
        self._people = People(people)

    def people(self):
        return self._people

    def matches(self):
        return Pairs(self._people)
