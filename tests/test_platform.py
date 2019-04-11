import pytest


def test_testplatform():
    from zillean_client import load
    load('http://localhost:8888/api/v1/')
    from  zillean_client.file import file as fileapi
    api = fileapi(project={'api_root': 'http://localhost:8888/api/v1/', 'name': 'test'})
    print(api.project['name'])
    print(api.list())

def test_project():
    from zillean_client import load
    load('http://localhost:8888/api/v1/')
    from  zillean_client.project import project as projectapi
    api = projectapi(project={'api_root': 'http://localhost:8888/api/v1/', 'name': 'test'})
    print(api.project['name'])
    print(api.list())

def test_tag():
    from zillean_client import load
    load('http://localhost:8888/api/v1/')
    from  zillean_client.tag import tag as tagapi
    api = tagapi(project={'api_root': 'http://localhost:8888/api/v1/', 'name': 'test'})
    print(api.list())
