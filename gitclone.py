#!/usr/bin/python

import sys
import re
import os

args = sys.argv

if len(args) == 1:
	print('usage: python gitclone.py {git ssh href}')
	quit()

if re.search(ur'^git@git(hub|lab).com:.+/.+.git$', args[1]):
	print('processing...')
else:
	print('your git ssh href is invalid, you have to provide ssh href like format: git@github.com:YOUR_USERNAME/YOUR_PROJECT_NAME.git')
	quit()

gitHref = args[1]

emails = []
configFile  = open("example_config", "r")

# loop lines from file for host retreival
for line in configFile:
	if re.match('^Host (.+)', line):
		result = re.match('^Host (.+)', line)
		emails.append(result.group(0))

# print email for selection
print('found emails: ')
for email in emails:
	print email

selectedHost = raw_input("Select the host, or enter username: ")

# ssh href 
didGitHrefContainsUsername = re.search(ur'git(hub|lab).com:(.+)/', gitHref)

gitHrefWithHost = ''
if didGitHrefContainsUsername:
	gitHrefWithHost = gitHref.replace(didGitHrefContainsUsername.group(2), selectedHost)
	print('fetching git:' + gitHrefWithHost)
	os.system('git clone ' + gitHrefWithHost)
else:
	print('unknown error')
	exit()

