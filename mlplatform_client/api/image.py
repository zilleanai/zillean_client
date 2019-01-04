import requests
from io import BytesIO
from PIL import Image

from ..project import Project

class image():
    def __init__(self, project: Project):
        self.project = project

    def list(self):
        url = 'https://'+self.project.api_root() + '/image/list/' + str(self.project.name)
        return requests.get(url).json()['files']

    def download(self, img_name:str):
        url = 'https://'+self.project.api_root() + '/image/download/' + str(self.project.name) + '/' + img_name
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))
        return img

    def thumbnail(self, img_name:str):
        url = 'https://'+self.project.api_root() + '/image/thumbnail/' + str(self.project.name) + '/' + img_name
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))
        return img
        