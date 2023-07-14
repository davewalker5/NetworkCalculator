#!/bin/zsh -f

clear

export PROJECT_ROOT=$( cd "$(dirname "$0")" ; pwd -P )
source "$PROJECT_ROOT/venv/bin/activate"
export PYTHONPATH="$PROJECT_ROOT/src"

python -m cli
