#!/usr/bin/env python3
"""updating of the init.py"""

import models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
