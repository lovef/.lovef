#!/usr/bin/env bash

dir=$( dirname "${BASH_SOURCE[0]}" )
fullpath="$( cd $dir ; pwd -P )"

source $dir/.bash_prompt

realpath() {
    [[ $1 = /* ]] && echo "$1" || echo "$PWD/${1#./}"
}

dir=$(realpath "$dir")

function title {
    if [ ! -z "$*" ]; then
        title_set=true
        echo -ne "\033]0;"$*"\007"
    else
        title_set=false
    fi
    source $dir/.bash_prompt
}
