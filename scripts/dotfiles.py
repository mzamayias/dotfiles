import os
from pprint import pprint


def list_dotfiles_dotdirectories() -> dict:
    """
    List all dotfiles and dotdirectories in the home directory.

    Returns:
        dict: A dictionary of dotfiles, dotdirectories and symbolic links.
    """
    # create a list to store all dotfiles
    dotfiles = []
    dotdirectories = []
    symlinks = []
    # create a list to store all files in the home directory
    items = os.listdir('/Users/mzamayias')
    # loop through the files in the home directory
    for item in items:
        # if the file starts with a dot, add it to the dotfiles list
        if item.startswith('.'):
            dotentry = os.path.join('/Users/mzamayias', item)
            if os.path.isfile(dotentry):
                dotfiles.append(dotentry)
            if os.path.isdir(dotentry):
                dotdirectories.append(dotentry)
            if os.path.islink(dotentry):
                symlinks.append(dotentry)
    # return the dotfiles list
    return {'dotfiles': dotfiles, 'dotdirectories': dotdirectories, 'symbolic_links': symlinks}


def move_dotentry(dotentry: str) -> None:
    """
    Moves a dotentry into the `dotfiles` or `dotdirectories` directory respectively.

    Args:
        dotentry (str): The dotentry to move.
    """
    try:
        if os.path.isfile(dotentry):
            os.rename(dotentry, os.path.join('/Users/mzamayias/dotfiles', dotentry))
        elif os.path.isdir(dotentry):
            os.rename(dotentry, os.path.join('/Users/mzamayias/dotdirectories', dotentry))
        else:
            print(f'Error: {dotentry} is not a dotentry.')
            raise Exception('Invalid dotentry.')
    except Exception as e:
        print(e)


def link_dotentry(dotentry: str) -> None:
    """
    Creates a symbolic link in the home directory.

    Args:
        dotentry (str): The dotentry to link.
    """
    try:
        if not (os.path.islink(dotentry)):
            os.symlink(dotentry, os.path.join('/Users/mzamayias', dotentry))
    except Exception as e:
        print(e)


def create_dotentry(dotentry: str) -> None:
    """
    Creates a dotentry. A dotentry is a dotfile or a dotdirectory that has been moved into the `dotfiles` or
    `dotdirectories` directory respectively and has a symbolic link in the `home` directory. Performs check that the
    dotfile or dotdirectory exists in the home directory and is not a symbolic link.

    Args:
        dotentry (str): The dotentry to create.
    """
    if not (os.path.islink(path=dotentry)):
        if os.path.isfile(dotentry) or os.path.isdir(dotentry):
            if os.path.isfile(dotentry):
                print(f'{dotentry} is a dotfile')
            elif os.path.isdir(dotentry):
                print(f'{dotentry} is a dotdirectory')
            # move_dotentry(dotentry)
            # link_dotentry(dotentry)
    else:
        print(f'{dotentry} is a symbolic link')


def get_info(dotentry_data: dict) -> None:
    """
    Outputs information about the dotentries. Prints the total number of dotentries and the number of dotfiles in the
    home directory.

    Args:
        dotentry_data (dict): The dotentries to get information about.
    """
    number_of_dotfiles = len(dotentry_data['dotfiles'])
    number_of_dotentries = len(dotentry_data['dotdirectories'])
    number_of_symbolic_links = len(dotentry_data['symbolic_links'])
    print(f'Total number of dotentries to create: {number_of_dotentries + number_of_dotfiles}')
    print(f'Number of dotfiles to create: {number_of_dotfiles}')
    print(f'Number of dotdirectories to create: {number_of_dotentries}')
    print(f'Number of symbolic links already in place: {number_of_symbolic_links}')


def find_in_dotentries(data: dict) -> None:
    """
    Asks user to enter the name of a dotentry. It searches the data dictionary for the dotentry and returns the path of
    the dotentry.

    Args:
        data (dict): The dotentries to find.
    """
    dotentry = input('Enter the name of a dotentry: ')
    for key in data:
        for item in data[key]:
            if item.endswith(dotentry):
                print(f'\nFound dotentry: {dotentry} at {item} in {key}')


if __name__ == '__main__':
    # call the list_dotfiles function
    dotentries = list_dotfiles_dotdirectories()
    get_info(dotentries)
    # print the dotfiles
    create_dotentry(dotentries['dotfiles'][10])
    # call cat on dotfiles['dotfiles'][0]
    os.system(f"cat {dotentries['dotfiles'][10]}")
    find_in_dotentries(data=dotentries)
    # # call the copy_dotfiles function
    # move_dotfiles(dotfiles)
    # # print a message
    # print('Done!')
    # # call the link_dotfiles function
    # link_dotfiles(dotfiles)
    # # print a message
    # print('Done!')
