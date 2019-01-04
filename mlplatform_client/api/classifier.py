# source: https://stackoverflow.com/questions/44463768/python3-requests-post-ignoring-filename-when-using-bytesio
import requests
from io import BytesIO
from PIL import Image

from ..project import Project


class classifier():
    def __init__(self, project: Project):
        self.project = project

    def predict(self, image: Image):
        url = 'https://'+self.project.api_root() + '/classifier/predict/' + \
            str(self.project.name)
        img_io = BytesIO()
        image.save(img_io, 'JPEG', quality=80)
        file = img_io.getvalue()
        action = {"filepond": ('predict.jpg', file)}
        response = requests.post(url, files=action)
        return response.json()['prediction']
