@echo off
REM Activar entorno virtual python en carpeta "env"

REM comprobar si la carpeta "env" existe
IF NOT EXIST env (
    echo la carpeta "env" no existe.
    pause
    exit /b
)

REM activar entorno virtual (windows)
call env\Scripts\activate.bat

REM cONFIRMACION
ECHO Entorno virtual activado.

cd tienda_videojuegos

python manage.py runserver

cmd /k