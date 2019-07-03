import argparse
import git
import json
import os
import sys

if __name__ == "__main__":

    parser=argparse.ArgumentParser()
    parser.add_argument("--config", "-c", type=str)

    args=parser.parse_args()
    config = args.config
    cwd = os.getcwd()

    try:
        with open(config) as f:
            config_data = json.load(f)

        project_name = config_data["project_name"]
        repo_name = config_data["repo_name"]
        author_name = config_data["author_name"]
        description = config_data["description"]
        python_interpreter = config_data["python_interpreter"]

    except TypeError as e:
        print("Config file not provided")
        sys.exit()
    except KeyError as e:
        print(f"KeyError, config does not contain key {e}")
        sys.exit()
    except:
        print(f"Unexpected error: {sys.exc_info()[0]}")
        raise

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
    