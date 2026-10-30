"""
Markdown Export Module for CampusNotes.
Contributed by Divjot Singh (PR #2).
"""
import os
from typing import Optional

def format_note_as_markdown(raw_text: str, title: str = "Note") -> str:
    """Converts raw lecture notes into formatted Markdown."""
    return f"# {title}

{raw_text}
"

def export_to_file(raw_text: str, title: str, output_dir: str = "exports") -> str:
    """Exports formatted markdown to file safely with UTF-8 encoding."""
    os.makedirs(output_dir, exist_ok=True)
    filepath = os.path.join(output_dir, f"{title.lower().replace(' ', '_')}.md")
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(format_note_as_markdown(raw_text, title))
    return filepath
