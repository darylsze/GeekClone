# GeekClone
easy python script to perform 'git clone' for multiple git user accounts

# Prerequisite:
- prepare config file under ~/.ssh
- its file structure should be like
```
Host gitlab.com-windsze
HostName gitlab.com
User git
PreferredAuthentications publickey
IdentityFile {YOUR SSH PRIVATE KEY LOCATION}
UseKeychain yes
AddKeysToAgent yes
```
- if you have multiple accounts, make sure add them all in your config file
```
# ---- Config for user whose name is Daryl ---
Host gitlab.com-daryl
HostName gitlab.com
User git
PreferredAuthentications publickey
IdentityFile {YOUR SSH PRIVATE KEY LOCATION}
UseKeychain yes
AddKeysToAgent yes
# ---- End of Config for user whose name is Sunny ---

# ---- Config for user whose name is Sunny ---
Host gitlab.com-sunny
HostName gitlab.com
User git
PreferredAuthentications publickey
IdentityFile {YOUR SSH PRIVATE KEY LOCATION}
UseKeychain yes
AddKeysToAgent yes
# ---- End of Config for user whose name is Sunny ---
```

# How to start:
1. on your terminal 
```sh
$ python GeekClone.py {git repo ssh href, for example: git@github.com:plateaukao/CalliImageView.git}
```
2. Will ask for your username or host name
3. enter your username, it will do git clone for you 
