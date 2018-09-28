#!/usr/bin/env bash

set -e

PROJECT_NAME=""
PROJECT_PATH=""

while [ -z "$PROJECT_NAME" ]
do
    echo "Please enter the the new project name:"
    read -rp ">" PROJECT_NAME
done

while [ -z "$PROJECT_PATH" ]
do
    echo "Please enter the the new project path:"
    read -rp ">" PROJECT_PATH
done


django-admin startproject --template ./django_project_template --extension=py,md,lock,cfg,yml,yaml --name .editorconfig,.gitignore,Pipfile,Procfile,.bandit "$PROJECT_NAME" "$PROJECT_PATH"