#!/usr/bin/env bash

PROJECT_ROOT=$( cd "$( dirname "$0" )/.." && pwd )
. "$PROJECT_ROOT/venv/bin/activate"

pip freeze --local | grep -v '^\-e' | cut -d = -f 1 | xargs -n1 pip3 install -U 
pip freeze > requirements.txt
