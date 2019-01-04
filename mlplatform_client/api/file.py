import requests
from io import BytesIO
from PIL import Image

from ..project import Project

class file():
    def __init__(self, project: Project):
        self.project = project

    def list(self, path:str = ''):
        url = 'https://'+self.project.api_root() + '/file/list/' + str(self.project.name) + '/' + path
        return requests.get(url).json()['files']

    def download(self, file_name:str):
        url = 'https://'+self.project.api_root() + '/file/download/' + str(self.project.name) + '/' + file_name
        response = requests.get(url)
        data = BytesIO(response.content)
        return data

    def tags(self, file_name:str):
        url = 'https://'+self.project.api_root() + '/file/tags/' + str(self.project.name) + '/' + file_name
        return requests.get(url).json()['tags']