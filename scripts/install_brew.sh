#!/bin/bash

install_homebrew() {
    # Installs Homebrew
    echo /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)" >>./.install_brew_log
    if /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)" 2>>./.install_brew_log; then
        echo "Successfully installed Homebrew." 2>&1 | tee -a ./.install_brew_log
    else
        echo "Failed to install Homebrew." 2>&1 | tee -a ./.install_brew_log
        return 1
    fi
}
