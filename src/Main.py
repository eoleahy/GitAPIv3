from github import Github
from flask import Flask, render_template,request
import json     #json for data
import webbrowser #open web page
import os       #get cwd

app = Flask(__name__)

# using username and password
@app.route('/',methods=['POST','GET'])
def home():


    if request.method == "POST":
        username = request.form['username']
        pswd = request.form['password']

        handle_input(username,pswd)
        json_data = send_Json()
        return render_template('socialGraph.html', json_data= json_data)

    return render_template('socialGraph.html')

def send_Json():

    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT,"static/","data.json")
    data =json.load(open(json_url))
    print("sending json")

    return data


def handle_input(username,pswd):

    g = Github(username,pswd)
    user = g.get_user()

    json_arr=[]
    my_repositories = user.get_repos()

    #print logged in user as the "root"
    print(user.login)
    #iterate through repos
    for my_repo in my_repositories:

        i = 0
        contributors = my_repo.get_contributors()
        for users_contrib in contributors:
            i+=1

        json_repo = {
            "name": my_repo.name,
            "value": i
        }

        json_arr.append(json_repo)

    with open('src/static/data.json','w') as outfile:
        json.dump(json_arr, outfile)




if __name__ == '__main__':
    print("Opening in browser")
    webbrowser.open_new_tab("http://localhost:5000")
    app.run()
