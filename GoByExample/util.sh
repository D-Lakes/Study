#!/bin/bash

# I was getting a warning about main being redeclared
# Per Jonathan Hall on StackOverFlow this is the only solution
# https://stackoverflow.com/questions/66970531/vs-code-go-main-redeclared-in-this-block
# aliased to 'g'

if [ "$#" -ne 1 ]; then
  echo "you forgot the filename or something"
  exit 1
fi


mkdir $1 && lvim ./$1/$1.go || nvim $1.go
