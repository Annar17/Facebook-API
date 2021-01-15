import truffleHog
from bs4 import BeautifulSoup
import urllib3
from subprocess import call

# Code in Python3

#Some basic set-up for bs
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
git_url = "https://github.com"
git_monthly = "https://github.com/trending?since=monthly"

http = urllib3.PoolManager()
response = http.request('GET', git_monthly)
data_soup = BeautifulSoup(response.data, 'html.parser')

data_soup = data_soup.main.find('div',{'class':'explore-pjax-container container-lg p-responsive pt-6'})
data_soup = data_soup.findAll('article',{"class":'Box-row'})

git_repos = ["/facebook/flipper"]

for repo in data_soup:
    git_repos.append(repo.h1.a['href'])

print("\nScanning the most trending repositories of the month.\n")

for repo in git_repos:
    url = git_url+repo
    print("Searching for API Keys in %s repository. Please wait...\n"%url)
    call(["trufflehog","--regex","--entropy=False", url])
    print("      Finished searching.\n")
