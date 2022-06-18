# create a function called getDotfiles that returns all dotfiles from a directory
getDotfiles() {
  local dotfiles
  # get all files in given directory
  dotfiles=$(ls -a $1 .* | awk '{print $1}' | uniq | sort)
  # dotfiles=$(ls -a $1 | grep -v "^\.$" | grep -v "^\.\..$")
  # dotfiles=$(find . -name ".*")
  # print each dotfile in a line
  for dotfile in $dotfiles; do
    echo $dotfile
  done
}

# create a function called copyDotfiles that copies dotfiles from a directory to the home directory
copyDotfiles() {
  local dotfiles
  local dotfile
  dotfiles=$(getDotfiles $1)
  for dotfile in $dotfiles; do
    cp -f $dotfile ~
  done
}

# create a function called linkDotfiles that creates symlinks from a directory to the home directory
linkDotfiles() {
  local dotfiles
  local dotfile
  dotfiles=$(getDotfiles $1)
  for dotfile in $dotfiles; do
    ln -fs $dotfile ~
  done
}

# create a function called installDotfiles that calls copyDotfiles and linkDotfiles
installDotfiles() {
  local dotfiles
  dotfiles=$(getDotfiles $1)
  copyDotfiles $dotfiles
  linkDotfiles $dotfiles
}

# create a function called installDotfiles that calls copyDotfiles and linkDotfiles
# installDotfiles $1
getDotfiles $1
