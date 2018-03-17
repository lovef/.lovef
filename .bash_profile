#!/usr/bin/env bash

# Source this in ~/.bash_profile

dir=$( dirname "${BASH_SOURCE[0]}" )

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
