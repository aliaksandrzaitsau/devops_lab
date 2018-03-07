import requests 
import json 
import argparse
import getpass

print ('Enter name:')
user=input()
passw = getpass.getpass(prompt="Enter password:")

parser = argparse.ArgumentParser()
parser.add_argument("-o","--opt",help="choose needed option \"Users names\" or \"Created date\" or \"Projects\" or \"Forks_count\" or \"Title\" for example \"python 2.py -o 'Forks_count'\"")
args = parser.parse_args()

#r = requests.get('https://api.github.com/repos/alenaPy/devops_lab/contributors', auth=("user", "passw")) 

#print(json.dumps(r.json(), indent = 4, ensure_ascii = False)) 
#json_dict = r.json()

#print('User login: ' + str(json_dict[0].get('login')))
#print('User id:    ' + str(json_dict[0].get('id')))
#print('User type:  ' + str(json_dict[0].get('type')))


repo = requests.get('https://api.github.com/repos/alenaPy/devops_lab/pulls' , auth=(user, passw)) 
 
json_dict = repo.json()

#print('User id:    ' + str(json_dict[0].get('head').get('pushed_at')))
#print('User type:  ' + str(json_dict[0].get('head').get('user').get('login')))


if args.opt == "Users names":
	number = len(json_dict)
	i = 0;
	for i in range(number):
		print('User name' + str(i + 1) + ':  ' + str(json_dict[i].get('head').get('user').get('login')))
		   
if args.opt == "Created date":
	number = len(json_dict)
	i = 0;
	for i in range(number):
		print('Created date:                ' + str(json_dict[0].get('head').get('repo').get("created_at")))  
		print('User name' + str(i + 1) + ': ' + str(json_dict[i].get('head').get('user').get('login')))	
	
if args.opt == "Projects":
	number = len(json_dict)
	i = 0;
	for i in range(number):
		print('User name' + str(i + 1) + ': ' + str(json_dict[i].get('head').get('user').get('login')))
		print('Projects true/folse:         ' + str(json_dict[0].get('head').get('repo').get("has_projects")))
		

if args.opt == "Forks_count":
	print('Forks_count:  ' + str(json_dict[0].get('base').get('repo').get('forks_count')))
	print('Owner:        ' + str(json_dict[0].get('base').get('user').get('login')))

if args.opt == "Title":
	number = len(json_dict)
	i = 0;
	for i in range(number):
		print('Title' + str(i + 1) + ': ' + str(json_dict[i].get('title')))
	
#else:
#	print("Sorry, choose other parametr or read --help\-h")


print('You see it because everything is fine!')









	


