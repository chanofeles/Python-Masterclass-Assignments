@echo off
:: --- NUKE VERSION ---
set NUKE_VERSION=Nuke13.2
set NUKE_PATH=C:\Program Files\%NUKE_VERSION%v4

:: --- START NUKE WITH FLAGS FOR NUKE X AND PAUSED VIEWER TO AVOID CRASHING ON HEAVY SCRIPTS---
"%NUKE_PATH%\%NUKE_VERSION%.exe" --nukex --pause