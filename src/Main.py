from github import Github
import getpass
import json

# using username and password
def main():
    username = input('Username:')
    pswd = getpass.getpass('Password:')
    g = Github(username, pswd)

    totalRepoList = None
    user = g.get_user()
    repos = user.get_repos()
    for repo in repos:
        print(repo.name)
        #repo.edit(has_wiki=False)
        # to see all the available attributes and methods
        contrib = repo.get_contributors()
        for users in contrib:
            print("     ", users.name)

    if(input('Press q to close: ') is 'q'):
        exit()

if __name__ == '__main__':
    main()
