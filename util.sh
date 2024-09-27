#!/bin/bash

# I was getting a warning about main being redeclared
# Per Jonathan Hall on StackOverFlow this is the only solution
# https://stackoverflow.com/questions/66970531/vs-code-go-main-redeclared-in-this-block
# aliased to 'g'
# Extending to work with .py or .go by adding 2nd argument
# E.G:
# g example go --> ./example/example.go
# g examply py--> ./example/example.py
# Makes test_example.py for pytesting

if [ "$#" -ne 2 ]; then
  echo "you forgot the file extension or something"
  exit 1
fi

if [ "$2" == "py" ]; then
  mkdir $1
  touch $1/test_$1.$2
  touch $1/$1.$2
  lvim $1/$1.$2 || nvim $1.$2
  else
    mkdir $1
    touch $1.$2
    lvim $1.$2 || nvim $1.$2
fi

