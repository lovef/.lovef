#!/usr/bin/env bash

# Source this in ~/.bash_profile

dir=$( dirname "${BASH_SOURCE[0]}" )
fullpath="$( cd $dir ; pwd -P )"

export PATH=${fullpath}/bin:$PATH

alias path-pretty='echo $PATH | tr ":" "\n"'

# https://stackoverflow.com/a/3466183/1020871
case "$(uname -s)" in
    Linux*);;
    Darwin*)
        source ${dir}/mac/.bash_profile
        ;;
    CYGWIN*);;
    MINGW*)
        source ${dir}/windows/.bash_profile
        ;;
    *);;
esac
