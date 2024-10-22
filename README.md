# 🚀 GitHub Repo & Project Automation Script

This Python script automates the creation of GitHub repositories and sets up local projects with Git.

## ⚙️ Requirements

- Python 3.x
- Git installed
- A GitHub token with permissions to create repositories

### Installation

1. Install the dependencies from `requirements.txt`:

```bash
pip install -r requirements.txt
```

2. Create a .env file with the following content:
```
GITHUB_TOKEN = "your_github_token"
PATH_PROJECT = "path/where/you/create/projects/"
URL_GITHUB = "https://github.com/your_github_username"
```

## 💻 Usage
```bash
python script.py <project_name>
```