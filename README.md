# mlplatform_client

client for mlplatform

## installation

```bash
pip install git+https://gitlab.chriamue.de/mlplatform/mlplatform_client.git
```

## usage

```python
from mlplatform_client import load
load('http://localhost:8888/api/v1/')
from mlplatform_client.tag import tag as tagapi
api = tagapi(project={'api_root': 'http://localhost:8888/api/v1/', 'name': 'test'})
print(api.list())
```