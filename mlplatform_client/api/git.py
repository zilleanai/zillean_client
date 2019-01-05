import os
from git import Repo
from ..project import Project


class git():
    def __init__(self, project: Project):
        self.project = project

    def clone(self, path: str = 'data/'):
        url = 'https://'+self.project.api_root() + '/git/' + str(self.project.name)
        repo = Repo.clone_from(url, os.path.join(path, self.project.name))
        return repo

    def pull(self, path: str = 'data/'):
        repo = Repo(os.path.join(path, self.project.name))
        o = repo.remotes.origin
        return o.pull()