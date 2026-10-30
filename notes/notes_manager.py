"""
Notes Manager with leak-free safe file reading.
"""
import os

def read_note_safely(filepath: str) -> str:
    if not os.path.exists(filepath):
        return ""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()
