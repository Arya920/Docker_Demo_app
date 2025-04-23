@echo off
echo Starting your daily dose of motivation...
start http://localhost:8501
docker run -p 8501:8501 motivation-app
pause
