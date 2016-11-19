import yaml
import random


class Person:
    def __init__(self, dict):
        self.name = dict['name']
        self.username = dict['username']

    def __str__(self):
        return '%s (%s)' % (self.name, self.username)


class People(list):
    _people = []

    def __init__(self, people):
        for x in people:
            self._people.append(Person(x))

        list.__init__(self, self._people)


class Pair:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return '%s <---> %s' % (self.a.name, self.b.name)


class Pairs(list):
    _pairs = []

    def __init__(self, people):
        while len(people) > 0:
            a = self._pop_list(people)
            b = self._pop_list(people)

            self._pairs.append(Pair(a, b))

        list.__init__(self, self._pairs)

    def __str__(self):
        ret = ''

        for x in pairs:
            ret += '%s\n' % x

        return ret.rstrip('\n')

    @staticmethod
    def _pop_list(my_list):
        indices = list(range(0, len(my_list)))

        x = random.choice(indices)
        y = my_list[x]

        del indices[x]
        del my_list[x]

        return y

data = open('people.yml', 'r')
people = People(yaml.load(data)['people'])
pairs = Pairs(people)
print(pairs)
