@ECHO OFF
CLS

SET PROJECT_ROOT=%~p0
CALL %PROJECT_ROOT%\venv\Scripts\activate.bat
SET PYTHONPATH=%PROJECT_ROOT%src

python -m cli %*
ECHO ON
