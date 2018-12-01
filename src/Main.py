from github import Github
import getpass  #no show password
import json     #json for data
import webbrowser #open web page
import os       #get cwd


# using username and password
def main():

    webPage = 'src/socialGraph.html'

    filename= 'file:///' +os.getcwd()+'/' + webPage
    print("Opening", filename, "in browser")
        webbrowser.open_new_tab(filename)

    username = input('Username:')
    pswd = getpass.getpass('Password:')
    g = Github(username,pswd)
    user = g.get_user()

    total_user_list = []
    total_repo_list = []
    json_arr=[]
    my_repositories = user.get_repos()

    total_repo_list.append(my_repositories)

    #print logged in user as the "root"
    print(user.login)
    #iterate through repos
    for my_repo in my_repositories:

        #avoid overlap by comparing my repos to the total list
        if(my_repo not in total_repo_list):
            total_repo_list.append(my_repo)
            print(" |_", my_repo.name)
            json_repo = {
                "repo": my_repo.name,
                "link_repo": "root",
                "owner": username
            }
            y = json.dumps(json_repo)
            json_arr.append(y)
        #    print(y)

        #contributors of each repo iterate similarly
        contributors = my_repo.get_contributors()
        for users_contrib in contributors:

            #avoiding recursion
            if(users_contrib not in total_user_list and user.login != users_contrib.login):
                total_user_list.append(users_contrib)
                print("    |_", users_contrib.login)

                #getting contributors' repos
                contrib_repos = users_contrib.get_repos()

                for repo in contrib_repos:
                    if(repo not in total_repo_list):
                        total_repo_list.append(repo)
                        print("     |_", repo.name)

                        json_repo = {
                            "repo": repo.name,
                            "link_repo": my_repo.name,
                            "owner": users_contrib.login
                        }
                        y = json.dumps(json_repo)
                        json_arr.append(y)

    print(total_user_list)
    '''
    for i in total_repo_list:
        print(i)

    '''
    for j in json_arr:
        print(j)

    with open('src/data.json','w') as outfile:
        json.dump(json_arr, outfile)

    if(input('Press q to close: ') is 'q'):
        exit()




if __name__ == '__main__':
    main()
