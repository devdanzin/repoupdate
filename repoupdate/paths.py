import contextlib
import os
import pathlib
import typing


@contextlib.contextmanager
def chdir(target_path: pathlib.Path) -> typing.Iterator[pathlib.Path]:
    """
    Temporarily `cd` to a given directory.
    """
    previous_cwd = os.getcwd()
    try:
        os.chdir(target_path)
        yield target_path
    except OSError as e:
        print(f"Error opening directory {target_path}: {e}")
        raise
    finally:
        os.chdir(previous_cwd)


def get_subdirectories(paths: tuple[pathlib.Path, ...]) -> list[pathlib.Path]:
    result = []
    for path in paths:
        path = path.expanduser().resolve()
        for entry in path.iterdir():
            if entry.is_dir():
                result.append(entry)
    return result
