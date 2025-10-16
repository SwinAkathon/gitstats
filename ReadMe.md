## Dependencies
- PyGithub

## Procedure for analysing Git commit logs
1. Prepare data file: e.g. `data/teams.csv`
2. Open the Python notebook `gitstats.ipynb` and change configuration parameters in the first cell
3. Execute `Run-All` on the notebook

## Procedure for cloning Git repositories

- Run `python git_clone.py [file:teams.csv]`
  e.g. `python git_clone.py data/teams.csv`