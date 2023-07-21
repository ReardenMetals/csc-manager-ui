@ECHO OFF
setlocal
set KEYGEN_CORE=..\keygen-core-0.2.0\
set KEYGEN_PLUGINS=..\keygen-plugins-1.1.0\
set UI_DEPENDENCIES=..\ui-dependencies-win\
set PYTHONPATH=%KEYGEN_CORE%;%KEYGEN_PLUGINS%;%UI_DEPENDENCIES%;%PYTHONPATH%

echo KEYGEN_CORE = %KEYGEN_CORE%
echo KEYGEN_PLUGINS = %KEYGEN_PLUGINS%
echo UI_DEPENDENCIES = %UI_DEPENDENCIES%
echo PYTHONPATH = %PYTHONPATH%

python csc-manager.py
endlocal
pause