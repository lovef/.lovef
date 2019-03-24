#!/usr/bin/env bash

dir=$( dirname "${BASH_SOURCE[0]}" )
fullpath="$( cd $dir ; pwd -P )"

source $dir/../mac/.bash_prompt

function wslcode {
    code $(pathsToWin "$@")
}
alias code='wslcode'

function open {
    explorer.exe $(pathsToWin "$@")
}

function pathsToWin {
    parameters=''
    for var in "$@"
    do
        if [[ $var =~ ^- ]]; then
            parameters+="$var "
        else
            parameters+="$(wslpath -m $(realpath "$var")) "
        fi
    done
    echo $parameters
}

command -v gitk.exe >/dev/null 2>&1 && alias gitk=gitk.exe
