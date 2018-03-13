"""homework5"""
# pylint: disable=invalid-name
# pylint: disable=line-too-long
import argparse
import getpass
import requests


parser = argparse.ArgumentParser()
parser.add_argument("-o", "--opt",
                    help="""choose needed option |Users names|
                    or |Created date| or |Projects| or |Forks_count|
                    or |Title| for example |python 2.py -o Forks count|""")
parser.add_argument('-v', '--version',
                    action='version', help="Shows program's version",
                    version="1.2.0 Closed Beta Trial")
args = parser.parse_args()

print('Enter name:')
user = input()
passw = getpass.getpass(prompt="Enter password:")


repo = requests.get('https://api.github.com/repos/alenaPy/devops_lab/pulls',
                    auth=(user, passw)
                   )
json_dict = repo.json()

if args.opt == "Users names":
    number = len(json_dict)
    i = 0
    for i in range(number):
        print('User name' + str(i + 1) + ':  ' +
              str(json_dict[i].get('head').get('user').get('login')))

if args.opt == "Created date":
    number = len(json_dict)
    i = 0
    for i in range(number):
        print('Created date:                ' +
              str(json_dict[0].get('head').get('repo').get("created_at")))
        print('User name' + str(i + 1) + ': ' +
              str(json_dict[i].get('head').get('user').get('login')))

if args.opt == "Projects":
    number = len(json_dict)
    i = 0
    for i in range(number):
        print('User name' + str(i + 1) + ': ' +
              str(json_dict[i].get('head').get('user').get('login')))
        print('Projects true/folse:         ' +
              str(json_dict[0].get('head').get('repo').get("has_projects")))

if args.opt == "Forks count":
    print('Forks_count:  ' +
          str(json_dict[0].get('base').get('repo').get('forks_count')))
    print('Owner:        ' +
          str(json_dict[0].get('base').get('user').get('login')))

if args.opt == "Title":
    number = len(json_dict)
    i = 0
    for i in range(number):
        print('Title' + str(i + 1) + ': ' + str(json_dict[i].get('title')))


print('You see it because everything is fine!')
