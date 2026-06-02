# get pull_request information in a repo using python

# import requests module
import requests
from collections import Counter

# get github pull requests api
list1 = []
response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")
complete_details = response.json()
for i in range(len(complete_details)):
    list1.append((complete_details[i]["user"]["login"]))
counts = Counter(list1)
for key, value in counts.items():
    print(f"{key} made {value} pull_request")


