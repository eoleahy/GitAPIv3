from github import Github
import getpass  #no show password
import json     #json for data
import webbrowser
import os
# using username and password
def main():

    webPage = 'src/socialGraph.html'

    filename= 'file:///' +os.getcwd()+'/' + webPage
    print("Opening", filename, "in browser")
#    webbrowser.open_new_tab(filename)

    username = input('Username:')
    pswd = getpass.getpass('Password:')
    g = Github(username,pswd)

    totalRepoList = None
    user = g.get_user()
    repos = user.get_repos()
    for repo in repos:
        print(repo.name)
        #repo.edit(has_wiki=False)
        # to see all the available attributes and methods
        contrib = repo.get_contributors()
        for users in contrib:
            print("|_", users.name)
            repos2 = user.get_repos()
        #    for rep in repos2:
        #        print("  |_", rep.name)

    if(input('Press q to close: ') is 'q'):
        exit()

if __name__ == '__main__':
    main()
