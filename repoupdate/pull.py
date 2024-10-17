import os
import pathlib
import subprocess
import sys

from repoupdate.paths import chdir, get_subdirectories


def git_pull(path_list: list[pathlib.Path]) -> None:
    for path in path_list:
        print(f"## Pulling {path}:")
        with chdir(path):
            subprocess.run(["git", "pull"], stdout=sys.stdout, stderr=sys.stderr)
        print(f"Done.\n")


if __name__ == "__main__":
    cwds = (pathlib.Path(os.getcwd()),)
    git_pull(get_subdirectories(cwds))
