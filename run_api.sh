#!/bin/bash -f

clear

export PROJECT_ROOT=$( cd "$(dirname "$0")" ; pwd -P )
source "$PROJECT_ROOT/venv/bin/activate"
export PYTHONPATH="$PROJECT_ROOT/src"
export FLASK_DEBUG=1

echo Project root      = $PROJECT_ROOT
echo Python Path       = $PYTHONPATH
echo Flask Debug       = $FLASK_DEBUG

python -m api
