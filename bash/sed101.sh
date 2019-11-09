#!/bin/bash

# takes 2 arguments
# 1st - pattern to work with
# 2nd - file to run 

echo "sed test"

# $1 is the first argument
echo "argument1: $1 argument2: $2"

# remove the line from the file
# sed --in-place "/$1/d" $2

# replace the line
# sed "s/test*$1/test3/g" $2
sed -i "/$1/c\foo" $2
