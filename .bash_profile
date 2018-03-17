#!/usr/bin/env bash

# Source this in ~/.bash_profile

dir=$( dirname "${BASH_SOURCE[0]}" )
fullpath="$( cd $dir ; pwd -P )"

export PATH=${fullpath}/bin:$PATH

alias path-pretty='echo $PATH | tr ":" "\n"'

# https://stackoverflow.com/a/3466183/1020871
case "$(uname -s)" in
    Linux*);;
    Darwin*);;
    CYGWIN*);;
    MINGW*)
        source ${dir}/windows/.bash_profile
        ;;
    *);;
esac

# Gradle wrapper wrapper
function gw {
    command -v ./gradlew >/dev/null 2>&1 || { echo "Cannot find ./gradlew"; return; }
    if [[ $# == 2 && ($1 == "-v" || $1 == "--version") ]]; then
        echo "Let me update that wrapper for you ..."
        ./gradlew wrapper --gradle-version $2
        command -v dos2unix >/dev/null 2>&1 && dos2unix gradle/wrapper/gradle-wrapper.properties
    else
        ./gradlew $*
    fi
}
