#!/usr/bin/python3

"""
lockboxes - module contains one function
- fn => canUnlockAll
"""


def canUnlockAll(boxes):
    """
    - fn => canUnlockAll
    - params => boxes
    """
    if not boxes:
        return False

    visited = [False for i in range(len(boxes))]
    visited[0] = True
    queue = [0]

    while queue:
        current_box = queue.pop(0)
        for key in boxes[current_box]:
            if not visited[key]:
                visited[key] = True
                queue.append(key)

    return all(visited)
