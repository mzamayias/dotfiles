#!/bin/bash

install_ohmyzsh() {
    # Installs ohmyzsh
    echo sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" >>./.install_ohmyzsh
    if sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" 2>>./.install_ohmyzsh; then
        echo "Successfully installed ohmyzsh." 2>&1 | tee -a ./.install_ohmyzsh
    else
        echo "Failed to install ohmyzsh." 2>&1 | tee -a ./.install_ohmyzsh
        return 1
    fi
}

install_ohmyzsh
