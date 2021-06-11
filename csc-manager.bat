@ECHO OFF
setlocal
set KEYGEN_CORE=..\keygen-core\
set UI_DEPENDENCIES=..\ui-dependencies-win\
set PYTHONPATH=%KEYGEN_CORE%;%UI_DEPENDENCIES%;%PYTHONPATH%

echo KEYGEN_CORE = %KEYGEN_CORE%
echo UI_DEPENDENCIES = %UI_DEPENDENCIES%
echo PYTHONPATH = %PYTHONPATH%

python csc-manager.py
endlocal
pause