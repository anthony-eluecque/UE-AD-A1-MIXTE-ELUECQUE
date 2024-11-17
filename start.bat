@echo off
REM Script pour builder et démarrer un projet Docker Compose
REM Assurez-vous que Docker Compose est installé et accessible depuis la ligne de commande.

echo --- Docker Compose Build ---
docker-compose build
IF %ERRORLEVEL% NEQ 0 (
    echo Une erreur est survenue pendant la construction des images Docker.
    pause
    exit /b %ERRORLEVEL%
)

echo --- Docker Compose Up ---
docker-compose up -d
IF %ERRORLEVEL% NEQ 0 (
    echo Une erreur est survenue pendant le demarrage des conteneurs Docker.
    pause
    exit /b %ERRORLEVEL%
)

echo --- Operations terminees avec succes ---
pause
exit
