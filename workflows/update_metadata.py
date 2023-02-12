
# Tento nastroj slouzi k aktualizaci metadat v repozitari MLAB modulu 
# Je potreba ho spoustet z rootu repozitare

from github import Github
import yaml
from yaml import load, dump
from yaml import CLoader as Loader, CDumper as Dumper
import os

g = Github(os.environ['gh_token'])
repo_parameters = g.get_repo(os.environ['gh_repository'])
print(repo_parameters)

config_file = 'doc/metadata.yaml'
new = 0
stream = open(config_file, 'r')
stream.close()

data = yaml.full_load(stream)
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

#data['description'] = os.environ.get('gh_description', "Github Description")
data['github_url'] = os.environ.get('gh_url', "https://www.github.com/MLAB-project")
#data['github_org'] = os.environ.get('gh_org', 'repository_org')
data['github_repo'] = os.environ.get('gh_repo', "repository_name")
data['github_branch'] = os.environ.get('gh_branch', "repository_branch")

data['title'] = data['github_repo']

print(data)
yaml.dump(data, stream)
stream.close()
