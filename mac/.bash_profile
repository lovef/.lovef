#!/usr/bin/env bash

echo mac bash profile

dir=$( dirname "${BASH_SOURCE[0]}" )
fullpath="$( cd $dir ; pwd -P )"

source $dir/.bash_prompt
