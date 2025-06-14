import os
from pathlib import Path
import pytest


def test_api():
    from api import manager as man
    man.generateAPI()
    
def test_apiBuild():
    from api import manager as man
    d = Path(__file__).parent / 'temp'
    os.system(f'rm -rf {str(d)}')
    man.testAPI(d)
    os.system(f'rm -rf {str(d)}')
