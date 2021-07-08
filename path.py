"""Convenience functions for dealing with file paths and names."""
import os
from typing import List


def find(path='.', pattern='', ext='', antipattern='', include_path=True, absolute=False, sort=True) -> List:
    """Returns names of files in path that contain pattern, but not antipattern, and end with ext.

    By default, this returns filenames including the path.
    This behavior can be disabled by passing include_path=False.

    Args:
        path: directory to search in (may be absolute or relative). default: '.'
        pattern: string which must be contained in filename, leave empty to match all. default: empty
        ext: file extension to match
        antipattern: string which must NOT be contained in filename, empty does not filter anything. default: empty
        include_path: Include the path in the filenames? default: True
        absolute: Force return of absolute paths? default: False
        sort: Sort list before returning? default: True

    Returns:
        A list of file paths.
    """
    paths = [
            p                                                       # just the filename
            for p in os.listdir(path)                               # grab filenames
            if pattern in p                                         # check for pattern
            and ext in p[-len(ext):]                                # check for extension
            and (antipattern not in p or not antipattern)       # exclude antipattern
            ]
    if include_path:
        paths = [os.path.join(path, p) for p in paths]
        if absolute:
            paths = [os.path.abspath(p) for p in paths]     # resolve absolute paths
    if sort:
        paths.sort()    # Sort the paths in place, before returning
    return paths


def sort(paths: List) -> List:
    """Sorts a list of file paths and returns the sorted list.

    Args:
        paths: A (presumably unsorted) list of paths.

    Returns:
        List: A sorted list of paths.

    """
    paths.sort()
    return paths


def split(path: str) -> dict:
    """Splits a file path string into separate path, name, and extension components.

    Args:
        path: a file path consisting of a containing directory, a filename, and an extension

    Returns:
        A dict with the following keys:
        path: the path of the containing directory (will be empty if input is bare filename)
        name: the name of the file, without the extension
        ext: the file extension
    """
    path, name = os.path.split(path)
    name, ext = os.path.splitext(name)
    return {'path': path, 'name': name, 'ext': ext}
