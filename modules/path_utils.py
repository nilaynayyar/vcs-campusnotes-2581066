"""
Unified path resolution helper.
"""
import os

def resolve_note_path(filename: str, base_dir: str = 'notes') -> str:
    return os.path.abspath(os.path.join(base_dir, filename))
