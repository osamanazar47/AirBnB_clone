"""
create a unique FileStorage instance to the application
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
