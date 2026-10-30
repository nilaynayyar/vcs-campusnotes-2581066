"""
Student Progress Tracker and Module Analytics.
"""
import json

class ProgressTracker:
    def __init__(self):
        self.completed = set()

    def mark_completed(self, note_id: str):
        self.completed.add(note_id)

    def completion_percentage(self, total: int) -> float:
        if total == 0:
            return 0.0
        return (len(self.completed) / total) * 100.0
