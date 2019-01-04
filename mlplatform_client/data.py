import os
import requests
import re


class Data(object):
    def __init__(self, project):
        self.project = project
        self.data_dir = 'data'

    def __records(self):
        url = 'https://'+self.project.api_root() + '/record/records'
        return requests.get(url).json()

    def __record(self, id):
        url = 'https://'+self.project.api_root() + '/record/records/' + str(id)
        return requests.get(url).json()['record']

    def __len__(self):
        return len(self.__records())

    def __getitem__(self, index):
        records = []
        for record in self.__records():
            records.append(record['id'])
        return records[index]

    def filename(self, id):
        return self.__record(id)['filename']

    def download(self, id):

        download = self.filename(id)

        url = 'https://'+self.project.api_root() + '/record/csv/' + str(id)
        r = requests.get(url, stream=True)
        d = r.headers['content-disposition']
        download = re.findall("filename=(.+)", d)
        filename = os.path.join('data', self.project.name,
                                os.path.basename(download[0]))
        if not os.path.exists(filename):
            os.makedirs(os.path.join('data', self.project.name), exist_ok=True)

            with open(filename, "wb") as handle:
                for data in r.iter_content():
                    handle.write(data)
        return filename
