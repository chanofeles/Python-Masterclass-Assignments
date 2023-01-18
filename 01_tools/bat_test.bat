@echo off
:: --- NUKE VERSION ---
set NUKE_VERSION=Nuke13.2
set NUKE_PATH=C:\Program Files\%NUKE_VERSION%v4

:: --- SET PYTHON SCRIPT PATH ---
set PYTHON_PATH=E:\PythonMasterclass\assignments\01_tools

:: --- START NUKE WITH FLAGS FOR NUKE X AND PAUSED VIEWER TO AVOID CRASHING ON HEAVY SCRIPTS---
"%NUKE_PATH%\%NUKE_VERSION%.exe" --nukex --pause