import yaml
from SantaBot import SantaBot


if __name__ == '__main__':
    data = open('people.yml', 'r')
    santaBot = SantaBot(yaml.load(data)['people'])

    pairs = '%s' % santaBot.matches()
    print(pairs)
