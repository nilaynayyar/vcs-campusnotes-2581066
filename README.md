# CampusNotes

CampusNotes is a collaborative academic repository designed to organize study notes and educational resources.

## Project Structure

```text
Campus_Notes/
├── .githooks/
│   ├── commit-msg
│   └── pre-commit
├── notes/
│   └── data-structures.md
├── resources/
│   └── README.md
├── .gitignore
└── README.md
```

## Topics Covered

### Data Structures and Algorithms

- Linear Search
- Binary Search
- Bubble Sort
- Selection Sort

## Purpose

The purpose of CampusNotes is to provide an organized space where students can maintain academic notes, share learning resources, and collaborate using Git and GitHub.

## Collaboration Workflow

This project uses Git and GitHub for version control and collaboration.

1. Create a feature branch for new work.
2. Make changes to the project.
3. Commit changes with meaningful commit messages.
4. Push the feature branch to GitHub.
5. Create a Pull Request for review.
6. Merge approved changes into the main branch.

## Git Hooks

This repository uses shared Git hooks stored in the `.githooks/` directory.

- `pre-commit`: Runs checks before a commit is created.
- `commit-msg`: Validates commit messages.

These hooks help maintain consistency and quality across contributions.

## Contributing

Students can contribute by adding study notes, improving existing documentation, and sharing useful academic resources.

Please use descriptive branch names and meaningful commit messages when contributing.