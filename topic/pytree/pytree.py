try:
    from os import scandir
except ImportError:
    from scandir import scandir


def dry(entry):
    if isinstance(entry, str):
        entry = entry.split('/')
    length = len(entry)
    spaces = length*' '
    space = 4*spaces
    print(space + entry[-1])

def pytree(path):
    for entry in scandir(path):
        if entry.is_dir(follow_symlinks=False):
            dry(entry.path)
            yield from pytree(entry.path)
        else:
            yield entry

if __name__ == '__main__':
    import sys
    path = sys.argv
    dry(path)
    for entry in pytree(path if len(path) > 1 else '.'):
        dry(entry.path)
