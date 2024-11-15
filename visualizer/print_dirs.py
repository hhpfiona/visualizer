import os
from tm_trees import ordered_listdir


def print_items(d: str = os.path.join(".", "example-directory")
                , indentation: str = '') -> None:
    """
    A sample program showing how to recurse on directories using os.

    Print the list of files and directories in directory <d>, recursively,
    prefixing each with the given <indentation>.
    """
    for filename in ordered_listdir(d):
        subitem = os.path.join(d, filename)
        if os.path.isdir(subitem):
            print(indentation + filename + os.sep)
            print_items(subitem, indentation + '  ')
        else:
            print(indentation + filename)


if __name__ == '__main__':
    # As a default, we've specified PATH to be for the example
    # directory provided in the starter code zip file.
    PATH = os.path.join(".", "example-directory")
    print(f"calling print_items on path: {PATH}, "
          f"with base name: {os.path.basename(PATH)}")
    print_items(PATH)
