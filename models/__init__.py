"""init module"""

if __name__ == 'models':
    from models.engine.file_storage import FileStorage
else:
    from engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
