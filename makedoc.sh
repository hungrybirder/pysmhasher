#!/bin/bash

# set -x
CMD=$(which pandoc)
if [[ -z ${CMD} ]]; then
    echo "请安装pandoc"
else
    pandoc -f markdown -f rst -o README.rst README.md
fi


