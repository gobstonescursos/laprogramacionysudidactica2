@ECHO OFF
set indice=200
:SEGUIR
copy 002.png "%indice%.png"
set /A indice=1+%indice%
IF NOT EXIST 999.png GOTO :SEGUIR

