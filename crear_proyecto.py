import requests
import subprocess
import os
import sys
from dotenv import load_dotenv

load_dotenv()

github_token = os.getenv("GITHUB_TOKEN")
path_project = os.getenv("PATH_PROJECT")
url_github = os.getenv("URL_GITHUB")


def create_github_repo(repo_name):
    headers = {
        "Authorization": f"token {github_token}",
        "Accept": "application/vnd.github.v3+json"
    }
    data = {"name": repo_name}
    response = requests.post("https://api.github.com/user/repos", headers=headers, json=data)
    response.raise_for_status()
    print("Repository created.")


def create_project_folder(project_name):
    os.makedirs(path_project + project_name)
    print("Directory created.")


def initialize_git_repo(project_name):
    os.chdir(path_project + project_name)
    subprocess.run(["git", "init"])
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", "Initial commit"])
    print("Git repository intialized.")


def link_to_github_repo(project_name):
    os.chdir(path_project + project_name)
    subprocess.run(["git", "remote", "add", "origin", f"{url_github}/{project_name}.git"])
    subprocess.run(["git", "push", "-u", "origin", "main"])
    print("Repositorio local vinculado con el repositorio en GitHub.")


def create_empty_readme(project_name):
    with open(f"{path_project}{project_name}/README.md", "w") as f:
        pass


def main():
    if len(sys.argv) != 2:
        print("Use: python script.py <nombre_del_proyecto>")
        sys.exit(1)

    project_name = sys.argv[1]

    create_project_folder(project_name)
    create_github_repo(project_name)
    create_empty_readme(project_name)
    initialize_git_repo(project_name)
    link_to_github_repo(project_name)
    print("Proyecto y repositorio creados y vinculados exitosamente.")


if __name__ == "__main__":
    main()
