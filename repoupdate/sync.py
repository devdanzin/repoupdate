import logging
import os
import typing

import github3

logging.basicConfig(level=logging.DEBUG)

USER = os.environ["REPOUPDATE_USER"]
AUTH_TOKEN = os.environ["REPOUPDATE_AUTH_TOKEN"]


def sync_default_branches():
    user = github3.login(USER, token=AUTH_TOKEN)
    repositories: typing.Generator[github3.github.repo.ShortRepository] = user.repositories(
        number=5, sort="fullname"
    )

    for repo in repositories:
        full_repo: [github3.github.repo.Repository] = repo.refresh()
        default_branch: github3.github.repo.branch.Branch = full_repo.branch(full_repo.default_branch)
        print(f"Syncing branch {default_branch.name} in {full_repo.full_name}.")
        try:
            result = default_branch.sync_with_upstream()
            print(result)
            print("Done\n")
        except Exception as e:
            print(f"Failed to sync branch {default_branch.name}: {e}\n")


if __name__ == "__main__":
    print("## Syncing default branches.")
    sync_default_branches()