# __main__.yml
import santaslist
import yaml


data = open('test/people.yml', 'r')
santaslist.load_people(yaml.load(data)['people'])
print(santaslist.print_pairs())
