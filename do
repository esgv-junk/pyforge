#!/bin/bash

case "$1" in
    "html_docs") sphinx-build -b html docs docs/html;;     
    *)              
        echo "Available commands: html_docs";;
esac