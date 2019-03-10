#!/usr/bin/env bash

dir=$( dirname "${BASH_SOURCE[0]}" )
fullpath="$( cd $dir ; pwd -P )"

export PS1_WITH_GIT='\[\033]0;$TITLEPREFIX:${PWD//[^[:ascii:]]/?}\007\]\n\[\033[32m\]\A \u@\h \[\033[33m\]\w\[\033[36m\]`__git_ps1 " --> %s"`\[\033[0m\]\n$ '
export PS1_WITHOUT_GIT='\[\033]0;$TITLEPREFIX:${PWD//[^[:ascii:]]/?}\007\]\n\[\033[32m\]\A \u@\h \[\033[33m\]\w\[\033[0m\]\n$ '
export GIT_PS1_SHOWDIRTYSTATE=1
alias ps1_with_git='export PS1=$PS1_WITH_GIT'
alias ps1_without_git='export PS1=$PS1_WITHOUT_GIT'
ps1_without_git
command -v __git_ps1 >/dev/null 2>&1 && ps1_with_git

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
