import csv
import os
from github import Github
from git import Repo

import argparse

# Function to read the access token from a file
# @requires: access_token is kept in the single-line data file specified by `file_path`
def read_access_token(file_path='token'):
    with open(file_path, 'r') as file:
        token = file.readline().strip()
    return token

# personal access token stored in a file in the current directory
token_path = os.path.join(os.getcwd(), 'github-token')
token = read_access_token(token_path)

# Replace 'your_github_token' with your actual GitHub token
# Initialize the GitHub object
g = Github(token)

def clone_repo(repo_name, repo_dir_name):
    # Get the repository
    repo = g.get_repo(repo_name)

    # Get the repository clone URL (HTTPS or SSH)
    clone_url = repo.clone_url  # This gets the HTTPS URL
    # You can also use repo.ssh_url for SSH cloning if you have SSH set up

    # Clone the repository using GitPython
    # Define the folder structure
    base_dir = "repos"
    # repo_name = repo.name
    repo_folder = os.path.join(base_dir, repo_dir_name)

    # Ensure the base "repos" directory exists
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)

    # Ensure the subfolder for the repository exists
    if not os.path.exists(repo_folder):
        os.makedirs(repo_folder)

    # Clone the repository into the folder
    Repo.clone_from(clone_url, repo_folder)

    print(f"Repository '{repo_name}' cloned to {repo_folder}")

def process_teams(file_team):
    with open(file_team, 'r') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            team_name = row[0]
            print(f"Processing team {team_name}", end='...\n')
            # some teams have multiple repositories
            repos = row[1].split(';')
            
            # read each repo
            for repo in repos:
                print('repo URL: ', repo, end='...')
                repo_name1 = repo.split('/')[-2]
                repo_name2 = repo.split('/')[-1]
                repo_name = f'{repo_name1}/{repo_name2}'
                print('repo name: ', repo_name)
                clone_repo(repo_name, repo_name1+'_'+repo_name2)
            
            print('done')

if __name__ == '__main__':
    # process_teams('data/teams.csv')
    # Set up argument parsing
    parser = argparse.ArgumentParser(description='Process a CSV file of teams.')
    parser.add_argument('teamsFile', type=str, help='The path to the teams CSV file')

    # Parse the command-line arguments
    args = parser.parse_args()

    # Call the function with the input argument
    process_teams(args.teamsFile)