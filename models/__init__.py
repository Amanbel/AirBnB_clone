"""init module"""
import os
import sys

#fpath = os.path.join(os.path.dirname(__file__), 'models')
#sys.path.append(fpath)

if __name__ == 'models':
    from models.engine.file_storage import FileStorage
else:
    from engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
