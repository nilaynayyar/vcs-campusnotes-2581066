"""
Markdown Export Module for CampusNotes.
Contributed by Divjot Singh.
"""
import os

def format_note_as_markdown(raw_text: str, title: str = "Note") -> str:
    return f"# {title}\n\n{raw_text}\n"
