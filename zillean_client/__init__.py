import sys
import requests
from io import StringIO, BytesIO
import importlib
from importlib import import_module
import importlib.util
import importlib.machinery
import tempfile
import types


def load(host):
    url = host + 'pyclient/'
    modules = requests.get(url).json()['modules']
    print(__package__)
    for module in modules:
        try:
            print('importing module:', module)
            url = host + 'pyclient/' + module
            response = requests.get(url)
            fp = tempfile.NamedTemporaryFile()
            fp.write(response.content)
            fp.flush()

            modulename = __package__ + '.' + module
            mod = importlib.machinery.SourceFileLoader(
                module, fp.name).load_module()
            sys.modules[modulename] = mod
            fp.close()
        except Exception as e:
            print(e)
