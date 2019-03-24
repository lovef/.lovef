#!/usr/bin/env bash

dir=$( dirname "${BASH_SOURCE[0]}" )
fullpath="$( cd $dir ; pwd -P )"

alias open='start'

function explorer {
	explorer.exe $(pathsToWin "$@")
}

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

command -v powershell >/dev/null 2>&1 && alias say='powershell -File "$(cygpath -w "${fullpath}/speach.ps1")"'

function title {
    if [ ! -z "$*" ]; then
        export PS1='\n\[\033[32m\]\A \u@\h \[\033[33m\]\w\[\033[36m\]`__git_ps1 " --> %s"`\[\033[0m\]\n$ '
        echo -ne "\033]0;"$*"\007"
    else
        export PS1='\[\033]0;$TITLEPREFIX:${PWD//[^[:ascii:]]/?}\007\]\n\[\033[32m\]\A \u@\h \[\033[33m\]\w\[\033[36m\]`__git_ps1 " --> %s"`\[\033[0m\]\n$ '
        title_set=false
    fi
}

export GIT_PS1_SHOWDIRTYSTATE=1
title
