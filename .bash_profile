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

# Gradle wrapper wrapper
function gw {
    command -v ./gradlew >/dev/null 2>&1 || { echo "Cannot find ./gradlew"; return; }
    if [[ $# -gt 1 && ($1 == "-v" || $1 == "--version") ]]; then
        shift
        echo "Let me update that wrapper for you ..."
        echo "include this for complete distrubution: --distribution-type all"
        ./gradlew wrapper --gradle-version $*
        command -v dos2unix >/dev/null 2>&1 && dos2unix gradle/wrapper/gradle-wrapper.properties
    else
        ./gradlew $*
    fi
}
