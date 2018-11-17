from github import Github
import getpass

# using username and password
def main():
    username = input('Username:')
    pswd = getpass.getpass('Password:')
    g = Github(username, pswd)

    for repo in g.get_user().get_repos():
        print(repo.name)
        #repo.edit(has_wiki=False)
        # to see all the available attributes and methods

    if(input('Press q to close: ') is 'q'):
        exit()

if __name__ == '__main__':
    main()
