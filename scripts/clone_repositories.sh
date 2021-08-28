#!/bin/bash

clone_repositories() {
    # Clones all repositories from the given string array.
    #
    # Arguments:
    #   $1 - The directory to clone the repositories to.
    #   ("$@") - The array of repositories to clone.
    #
    # Returns:
    #   0 - Success
    #   1 - Failure
    #
    local directory=$1
    local repository_urls=("$@")
    for repository_url in "${repository_urls[@]:1}"; do
        repository_name="${repository_url##*/}"
        repository_name="${repository_name%.git}"
        repository_directory="$directory/$repository_name"
        echo "Cloning ${repository_name} to $repository_directory."
        echo git clone "${repository_url}" "${repository_directory}" >>./.clone_repositories_log
        if git clone "${repository_url}" "${repository_directory}" 2>>./.clone_repositories_log; then
            echo "Successfully cloned ${repository_name} to $repository_directory." 2>&1 | tee -a ./.clone_repositories_log
        else
            echo "Failed to clone ${repository_name} to $repository_directory. Exiting." 2>&1 | tee -a ./.clone_repositories_log
            return 1
        fi
    done
}

repository_urls=(
    'https://github.com/mzamayias/uni-work.git'
    'https://github.com/mzamayias/glowing-sniffle.git'
    'https://github.com/mzamayias/eHealth-Services-Semester-Project.git'
    'https://github.com/mzamayias/observer_pattern.git'
    'https://github.com/mzamayias/programming-languages.git'
    'https://github.com/mzamayias/hearts_game_sort_of.git'
)
directory="/Users/mzamayias/Documents/Repositories/Uni"
clone_repositories $directory "${repository_urls[@]}"

repository_urls=(
    'https://github.com/mzamayias/file_converter.git'
    'https://github.com/mzamayias/cold.git'
    'https://github.com/mzamayias/brawl-control.git'
    'https://github.com/mzamayias/game_2048.git'
)
directory="/Users/mzamayias/Documents/Repositories/Flutter"
clone_repositories $directory "${repository_urls[@]}"

repository_urls=(
    'https://github.com/mzamayias/expert-palm-tree.git'
    'https://github.com/mzamayias/my100daysofcode.git'
)
directory="/Users/mzamayias/Documents/Repositories/Miscellaneous"
clone_repositories $directory "${repository_urls[@]}"
