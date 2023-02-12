
# Tento nastroj slouzi k aktualizaci metadat v repozitari MLAB modulu 
# Je potreba ho spoustet z rootu repozitare

from github import Github
import yaml
from yaml import load, dump
from yaml import CLoader as Loader, CDumper as Dumper
import os

g = Github(os.environ['gh_token'])
repo = g.get_repo(os.environ['gh_repository'])
print(repo)

config_file = 'doc/metadata.yaml'
new = 0

try:
    stream = open(config_file, 'r')
    data = yaml.full_load(stream)
    stream.close()
except:
    print("Soubor neexistuje")
    data = None

stream = open(config_file, 'w+')
print(data, type(data))

if data:
    new = 0
else:
    data = {}
    data['homepage'] = True
    data['mark'] = 50
    new = 1

if new:
    pass

data['description'] = repo.description
data['github_url'] = os.environ.get('gh_url', "https://www.github.com/MLAB-project")
#data['github_org'] = os.environ.get('gh_org', 'repository_org')
data['github_repo'] = os.environ.get('gh_repo', "repository_name")
data['github_branch'] = os.environ.get('gh_branch', "repository_branch")
data['tags'] = repo.get_topics()

data['title'] = data['github_repo']

print(data)
yaml.dump(data, stream)
stream.close()