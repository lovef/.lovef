#!/usr/bin/env bash

function explorer {
	explorer.exe $(pathsToWin "$@")
}
alias open='explorer' # Consider using `start`

function code {
    code.cmd $(pathsToWin "$@")
}

function pathsToWin {
    parameters=''
    for var in "$@"
    do
        if [[ $var =~ ^- ]]; then
            parameters+="$var "
        else
            parameters+="$(cygpath -w "$var") "
        fi
    done
    echo $parameters
}
