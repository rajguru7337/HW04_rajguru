import requests


#  This function connects with github and displays the repositories along with number of commits in each repository
def git_rep(ID):
    url = "https://api.github.com/users/" + ID + "/repos" 
    response = requests.get(url) #  The git userID is being accessed
    content = response.json()
    if response.status_code != 200:  # checks if userID is not Valid
        print("User Invalid", response.status_code)
        return False
    for i in content: #  This loop displays number of commits in each repository under the userID
        url1 = "https://api.github.com/repos/" + ID + "/" + i['name'] + "/commits"
        response1 = requests.get(url1)
        content1 = response1.json()
        rep_name = i['name']
        length = len(content1)
        print("Repo: " + rep_name + " Number of commits: " + str(length))
    return True  # The function returns true when it is able to access each repository and display number of commits
