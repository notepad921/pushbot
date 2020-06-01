from .common import *

try:
    from .local import *
except ImportError:
    import os
    print(os.listdir())
    print('Can`t find local settings file, run command:')
    print('    cp settings/local.example.py settings/local.py')
    pass

from .dictionary import *
