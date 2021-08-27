#!/bin/bash

main() {
    # Run all scripts in current directory.
    for script in *.sh; do
        if [ "$script" != "main.sh" ]; then
            # Ask user to run current script. If they agree, run the script. Otherwise, skip it.
            echo "Run $script?"
            read -p "Y/n: " -n 1 -r
            echo
            if [[ $REPLY =~ ^[Yy]$ ]]; then
                echo "Running $script." 2>&1 | tee -a ./.main_log
                echo bash $script >>./.main_log
                if bash "$script" 2>>./.main_log; then
                    echo "Successfully ran $script." 2>&1 | tee -a ./.main_log
                else
                    echo "Failed to run $script." 2>&1 | tee -a ./.main_log
                    return 1
                fi
            else
                echo "Skipping $script." 2>&1 | tee -a ./.main_log
            fi
        fi
    done
}

main
