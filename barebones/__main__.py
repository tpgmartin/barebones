import git
import os
import sys

if __name__ == "__main__":

    # Get command line arguments
    cwd = os.getcwd()
    args = sys.argv
    # Handle missing parameters with `getopt`
    project_name = args[1]

    # Initialise git repository for new project folder
    repo_dir = os.path.join(cwd, project_name)
    r = git.Repo.init(repo_dir)

    # Create project directory structure
    project_structure = [project_name, "config", "test", "toolbox"]
    for directory in project_structure:
        path = os.path.join(repo_dir, directory)
        if not os.path.exists(path):
            os.makedirs(path)
        open(os.path.join(path, ".gitkeep"), 'w').close()

    # Create README
    with open(os.path.join(repo_dir, "README.md"), 'w') as tmp:
        tmp.write("#{}".format(project_name))
    