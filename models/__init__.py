"""the packege for the BaseModel class and its
    subclass
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
