# repoupdate

This is a little tool I use to sync some of my repositories on GitHub and git pull them
to their respective local clones.

Usage (well, this is more of a goal than what we have right now):
```
## Syncing GitHub default branches in remote repositories:

# Sync all GitHub repositories matching subdirectories of current directory.
repoupdate sync --all

# Sync all GitHub repositories  matching subdirectories of given path.
repoupdate sync --all ~/projects

# Sync specific GitHub repositories matching subdirectories of current directory.
repoupdate sync cpython pypy coveragepy

# Sync specific GitHub repositories matching given paths.
repoupdate sync ~/projects/cpython ../PycharmProjects/coveragepy


## Pulling from updated GitHub repositories:

# Pull from all repositories that are subdirectories of current directory.
repoupdate pull --all

# Pull from all repositories that are subdirectories of given path.
repoupdate pull --all ~/projects

# Pull from specific repositories that are subdirectories of current directory.
repoupdate pull cpython pypy coveragepy

# Pull from specific repositories in given paths.
repoupdate pull ~/projects/cpython ../PycharmProjects/coveragepy


## Using paths stored in a file:

repoupdate sync --input paths.txt
repoupdate pull --input paths.txt
```