import requests

#response = requests.get("https://api.github.com/repos/hashicorp/terraform/pulls")

response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")


# Object ouput

print(response)

# Object type

print(type(response))

# Url ouput, pull requests list

# print(response.json())

# api status whether it is successful or not

print(response.status_code)

# Let's obtain particular values from the pull requests information

Pull_Requests_Info = response.json()

print(Pull_Requests_Info[0]["url"])
print(Pull_Requests_Info[0]["id"])
print(Pull_Requests_Info[0]["user"]["login"])


# To get list of entire login details:

for i in range(len(Pull_Requests_Info)):
    print(Pull_Requests_Info[i]["user"]["login"])