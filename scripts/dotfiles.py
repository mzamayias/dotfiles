import os
from pprint import pprint


# create a function that lists all dotfiles in the home directory
def list_dotfiles_dotdirectories() -> dict:
    # create a list to store all dotfiles
    dotfiles = []
    dotdirectories = []
    # create a list to store all files in the home directory
    items = os.listdir('/Users/mzamayias')
    # loop through the files in the home directory
    for item in items:
        # if the file starts with a dot, add it to the dotfiles list
        if item.startswith('.'):
            entry = os.path.join('/Users/mzamayias', item)
            if os.path.isfile(entry):
                dotfiles.append(entry)
            elif os.path.isdir(entry):
                dotdirectories.append(entry)
    # return the dotfiles list
    return {'dotfiles': dotfiles, 'dotdirectories': dotdirectories}


# create a function that movies all dotfiles from the home directory to the dotfiles directory
def move_dotfiles(dotfiles: list) -> None:
    # loop through the dotfiles list
    for file in dotfiles:
        # create a source path
        source = os.path.join('/Users/mzamayias', file)
        # create a destination path
        destination = os.path.join('../dotfiles', file)
        # copy the file
        print(f'Moving {source} ➡️  {destination}')
        os.system(f'mv {source} {destination}')


# create a function that links all dotfiles from the dotfiles directory to the home directory
def link_dotfiles(dotfiles: list) -> None:
    # loop through the dotfiles list
    for file in dotfiles:
        # create a source path
        source = os.path.join(
            '/Users/mzamayias/Documents/Repositories/Miscellaneous/.dotfiles/dotfiles', file)
        # create a destination path
        destination = os.path.join('/Users/mzamayias', file)
        # link the file
        print(f'Linking {source} ➡️  {destination}')
        os.system(f'ln -s {source} {destination}')


if __name__ == '__main__':
    # call the list_dotfiles function
    dotfiles = list_dotfiles_dotdirectories()
    # print the dotfiles
    pprint(dotfiles['dotfiles'][0])
    # call cat on dotfiles['dotfiles'][0]
    # # call the copy_dotfiles function
    # move_dotfiles(dotfiles)
    # # print a message
    # print('Done!')
    # # call the link_dotfiles function
    # link_dotfiles(dotfiles)
    # # print a message
    # print('Done!')
