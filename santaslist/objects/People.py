class Person(object):
    name = None
    username = None

    def __init__(self, **person: dict) -> None:
        """
        Take a dictionary of name and username and convert to a Person object

        :param person:
        :rtype: None
        """
        assert 'name' in person and 'username' in person
        self.__dict__.update(person)

    def __str__(self) -> str:
        """
        Concat the name and username

        :rtype: str
        """
        return '%s (%s)' % (self.name, self.username)


class People(list):
    _people = []

    def __init__(self, people: list = []) -> None:
        """
        Take a list and convert it into People

        :param people:
        :rtype: None
        """
        assert isinstance(people, list)
        self._people = [Person(**x) for x in people]

        list.__init__(self, self._people)

    def __str__(self) -> str:
        """
        Join all People into a nice string

        :rtype: str
        """
        return ','.join(str(x) for x in self._people)
