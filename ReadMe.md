## Github repository
https://github.com/SwinAkathon/gitstats

## Dependencies
- PyGithub

## Running Gitstats on local machine
1. Open the Python notebook `gitstats.ipynb` and configure the parameters in the first cell
2. Uncomment and execute the code cells under `Setup` and `Ensure configuration (ONCE)`
   1. Once executed, revert the comment so that they are not executed subsequently each time
3. Execute `Run-All` on the notebook

## Running Gitstats on github.dev (cloud) using codespace
- Access Github repository page
- Open file `gitstats.ipynb`
- Under "More Edit Options" context menu, choose "Open with...github.dev"
- On `github.dev`'s Terminal, click the option to open the project on Github codespace.
- Follow the instructions to execute `gitstats.ipynb` the codespace.

## Procedure for cloning Git repositories

- Run `python git_clone.py [file:teams.csv]`
  e.g. `python git_clone.py data/teams.csv`