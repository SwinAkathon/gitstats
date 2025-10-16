## Dependencies
- PyGithub

## Procedure for analysing Git commit logs
1. Open the Python notebook `gitstats.ipynb` and configure the parameters in the first cell
2. Uncomment and execute the code cells under `Setup` and `Ensure configuration (ONCE)`
   1. Once executed, revert the comment so that they are not executed subsequently each time
3. Execute `Run-All` on the notebook

## Procedure for cloning Git repositories

- Run `python git_clone.py [file:teams.csv]`
  e.g. `python git_clone.py data/teams.csv`