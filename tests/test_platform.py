import pytest
from mlplatform_client import Project


def test_testplatform():
    from mlplatform_client.api import load
    load('http://localhost:8888/api/v1/')
    from  mlplatform_client.api.file import file as fileapi
    api = fileapi(project={'api_root': 'http://localhost:8888/api/v1/', 'name': 'test'})
    print(api.project['name'])
    print(api.list())
