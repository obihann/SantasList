import yaml
from SantasList import SantasList


if __name__ == '__main__':
    data = open('data/people.yml', 'r')
    santaBot = SantasList(yaml.load(data)['people'])

    pairs = '%s' % santaBot.matches()
    print(pairs)
