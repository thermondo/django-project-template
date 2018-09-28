#!/usr/bin/env bash

set -e

PROJECT_NAME=""
PROJECT_PATH=""

while [ -z "$PROJECT_NAME" ]
do
    echo "Please enter the new project name:"
    read -rp ">" PROJECT_NAME
done

while [ -z "$PROJECT_PATH" ]
do
    echo "Please enter the new project path:"
    read -rp ">" PROJECT_PATH
done

read -rp "Your project will be created on this path $PROJECT_PATH, please confirm (y/n)?" choice
echo
case "$choice" in
  y|Y );;
  n|N|* ) echo "Schade schade!";  exit 0;;
esac

mkdir -p "$PROJECT_PATH"
django-admin startproject --template ./django_project_template --extension=py,md,lock,cfg,yml,yaml --name .editorconfig,.gitignore,Pipfile,Procfile,.bandit "$PROJECT_NAME" "$PROJECT_PATH"
