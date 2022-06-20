import os

HOME_DIR_PATH = '/Users/mzamayias'
DOTFILE_REPOSITORY_PATH = '/Users/mzamayias/Documents/Repositories/Miscellaneous/dotfiles'
DOTFILE_LOCATION_PATH = '/Users/mzamayias/Documents/Repositories/Miscellaneous/dotfiles/dotfiles'


def list_dotfiles_dotdirectories(path: str) -> dict:
    """
    List all dotfiles and dotdirectories in the home directory.

    Returns:
        dict: A dictionary of dotfiles, dotdirectories and symbolic links.
    """
    # create a list to store all dotfiles
    dotfiles = []
    dotdirectories = []
    symlinks = []
    print(f'{path=}')
    # create a list to store all files in the home directory
    items = os.listdir(path)
    # loop through the files in the home directory
    for item in items:
        # if the file starts with a dot, add it to the dotfiles list
        if item.startswith('.'):
            dotentry = os.path.join(path, item)
            if os.path.islink(dotentry):
                symlinks.append(dotentry)
                continue
            if os.path.isfile(dotentry):
                dotfiles.append(dotentry)
                continue
            if os.path.isdir(dotentry):
                dotdirectories.append(dotentry)
                continue
    # return the dotfiles list
    return {'dotfiles': sorted(dotfiles), 'dotdirectories': sorted(dotdirectories), 'symlinks': sorted(symlinks)}


def move_dotentry(dotentry: str) -> None:
    """
    Moves a dotentry into the `dotfiles` or `dotdirectories` directory respectively.

    Args:
        dotentry (str): The dotentry to move.
    """
    try:
        if os.path.isfile(dotentry):
            os.rename(
                dotentry,
                os.path.join(DOTFILE_REPOSITORY_PATH, 'dotfiles', f'.{".".join(dotentry.split(".")[1:])}')
            )
        elif os.path.isdir(dotentry):
            os.rename(
                dotentry,
                os.path.join(DOTFILE_REPOSITORY_PATH, 'dotdirectories', f'.{".".join(dotentry.split(".")[1:])}')
            )
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
            os.symlink(
                src=dotentry,
                dst=dotentry.replace(DOTFILE_LOCATION_PATH, HOME_DIR_PATH)
            )
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
    if os.path.isfile(dotentry) or os.path.isdir(dotentry):
        print(f'Creating dotentry for {dotentry}')
        move_dotentry(dotentry)
        link_dotentry(dotentry)
    else:
        print(f'{dotentry} is a symbolic link')


def get_dotentries_info(dotentry_data: dict) -> None:
    """
    Outputs information about the dotentries. Prints the total number of dotentries and the number of dotfiles in the
    home directory.

    Args:
        dotentry_data (dict): The dotentries to get information about.
    """
    number_of_dotfiles = len(dotentry_data['dotfiles'])
    number_of_dotentries = len(dotentry_data['dotdirectories'])
    number_of_symbolic_links = len(dotentry_data['symlinks'])
    print(f'Total number of dotentries to create: {number_of_dotentries + number_of_dotfiles}')
    print(f'Number of dotfiles to create: {number_of_dotfiles}')
    print(f'Number of dotdirectories to create: {number_of_dotentries}')
    print(f'Number of symbolic links already in place: {number_of_symbolic_links}')


def find_in_dotentries(data: dict) -> dict:
    """
    Asks user to enter the name of a dotentry. It searches the data dictionary for the dotentry and returns the path of
    the dotentry.

    Args:
        :param data:  The dotentries to find.
    """
    query = input('Enter the name of a dotentry: ')
    results = {}
    for key in data:
        for item in data[key]:
            if query in item:
                results.update({'query': query, 'item': item, 'key': key})
    return results


def show_dotentry_info(dotentry: str) -> None:
    """
    Shows information about a dotentry.

    Args:
        dotentry (str): The dotentry to show information about.
    """
    if input(f'Show contents of {dotentry}? (y/n): ') == 'y':
        if os.path.isfile(dotentry):
            os.system(f'cat {dotentry}')


if __name__ == '__main__':
    # get_dotentries_info(list_dotfiles_dotdirectories(HOME_DIR_PATH))
    # for key, value in list_dotfiles_dotdirectories(HOME_DIR_PATH).items():
    #     if key == 'dotfiles':
    #         for item in value:
    #             # show_dotentry_info(item)
    #             create_dotentry(item)
    get_dotentries_info(list_dotfiles_dotdirectories(HOME_DIR_PATH))
    get_dotentries_info(list_dotfiles_dotdirectories(DOTFILE_LOCATION_PATH))
    for key, value in list_dotfiles_dotdirectories(DOTFILE_LOCATION_PATH).items():
        if key == 'dotfiles':
            for item in value:
                link_dotentry(item)
