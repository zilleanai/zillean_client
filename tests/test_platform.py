import pytest
from mlplatform_client import Project


def test_testplatform():
    from mlplatform_client.api import load
    load('http://localhost:8888/api/v1/')
    from  mlplatform_client.api.file import file as fileapi
    api = fileapi(project={'api_root': 'http://localhost:8888/api/v1/', 'name': 'test'})
    print(api.project['name'])
    print(api.list())

def test_project():
    from mlplatform_client.api import load
    load('http://localhost:8888/api/v1/')
    from  mlplatform_client.api.project import project as projectapi
    api = projectapi(project={'api_root': 'http://localhost:8888/api/v1/', 'name': 'test'})
    print(api.project['name'])
    print(api.list())

def test_tag():
    from mlplatform_client.api import load
    load('http://localhost:8888/api/v1/')
    from  mlplatform_client.api.tag import tag as tagapi
    api = tagapi(project={'api_root': 'http://localhost:8888/api/v1/', 'name': 'test'})
    print(api.list())
