#!/usr/bin/env bash

# Source this in ~/.bash_profile

dir=$( dirname "${BASH_SOURCE[0]}" )
fullpath="$( cd $dir ; pwd -P )"

export PATH=${fullpath}/bin:$PATH

alias path-pretty='echo $PATH | tr ":" "\n"'

# https://stackoverflow.com/a/3466183/1020871
case "$(uname -s)" in
    Linux*)
        source ${dir}/linux/.bash_profile
        ;;
    Darwin*)
        source ${dir}/mac/.bash_profile
        ;;
    CYGWIN*);;
    MINGW*)
        source ${dir}/windows/.bash_profile
        ;;
    *);;
esac

calc() {
    expression=$(echo $* | sed -E 's/,([^ ])/.\1/g' | \
        sed -E 's|//([0-9]+(\.[0-9]+)?)|sqrt(\1)|g' | \
        sed    's|//(|sqrt(|g' | \
        sed -E 's/([0-9)]) +([-+*/^]) ([(0-9])/\1\2\3/g' | \
        sed -E 's/(,? +)/,"\1",/g' | sed 's/\^/**/g' | sed 's/_//g')
    perl -E "say ($expression)"
}
