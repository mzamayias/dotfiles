#!/bin/bash

brew_bundle() {
    # Brews the bundle, executes `brew bundle`
    echo brew bundle >>./.brew_bundle_log
    if brew bundle 2>>./.brew_bundle_log; then
        echo "Successfully installed brew bundle." 2>&1 | tee -a ./.brew_bundle_log
    else
        echo "Failed to install brew bundle." 2>&1 | tee -a ./.brew_bundle_log
        return 1
    fi
}
