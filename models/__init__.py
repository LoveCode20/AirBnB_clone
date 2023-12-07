#!/usr/bin/env python3
"""updating of the init.py"""

from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
