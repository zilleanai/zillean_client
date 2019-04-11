# zillean_client

client for mlplatform

## installation

```bash
pip install git+https://github.com/zilleanai/zillean_client
```

## usage

```python
from zillean_client import load
load('http://localhost:8888/api/v1/')
from zillean_client.tag import tag as tagapi
api = tagapi(project={'api_root': 'http://localhost:8888/api/v1/', 'name': 'test'})
print(api.list())
```
