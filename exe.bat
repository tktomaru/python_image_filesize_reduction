@echo off
echo Running resize.py...
python resize.py
if %errorlevel% neq 0 (
    echo An error occurred while running resize.py.
    exit /b %errorlevel%
)

echo Running suggest.py...
python suggest.py
if %errorlevel% neq 0 (
    echo An error occurred while running suggest.py.
    exit /b %errorlevel%
)

echo Both scripts ran successfully.
pause
