# 🚀 Streamlit Docker App - Complete Guide (Windows Friendly)

This guide walks you through everything you need to know to containerize and run a Streamlit app using Docker, with additional tips for sharing via `.tar` file and `.bat` launcher scripts.

---

## 📁 Project Structure Example

your_project/ ├── app.py ├── Dockerfile ├── requirements.txt ├── models/ │ └── model.pkl ├── input_files/ │ └── data.csv └── run_app.bat

---

## 1️⃣ How to Create a Docker Image

First, make sure Docker is installed on your system: [Download Docker Desktop](https://www.docker.com/products/docker-desktop/)

Navigate to your project directory:
```bash
cd path\to\your_project
```


Build the image:
```bash
docker build -t motivation-app .
```

This creates an image named motivation-app.

2️⃣ What to Put in requirements.txt

Your requirements.txt should list all the Python packages your app needs. For a basic Streamlit app with ML models, it might look like:

streamlit
pandas
numpy
joblib
scikit-learn

Use the below code to auto-generate requirement file from your environment.
```bash
pip freeze > requirements.txt 
```

3️⃣ How to Write a Dockerfile

A good Dockerfile for a Streamlit app:

```bash
FROM python:3.11-slim

WORKDIR /app

# Copy all files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Streamlit's default port
EXPOSE 8501

# Run the app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

🔥 What to avoid:

    Avoid COPY-ing large unnecessary files (check .dockerignore)

    Avoid installing GUI packages or system tools not needed in a container

4️⃣ How to Build the Docker Image

In your terminal or PowerShell:

```bash
docker build -t motivation-app .
```

This command:

    - Reads the Dockerfile

    - Packages everything in the folder

    - Tags it as motivation-app

5️⃣ How to Run the App in Docker

After building the image, run:
```bash
docker run -p 8501:8501 motivation-app
```

Then open your browser at:

http://localhost:8501

6️⃣ Save Docker Image as .tar and Run It
🛑 Save the image as a .tar file:

```bash
docker save -o motivation-app.tar motivation-app
```

This creates a shareable file motivation-app.tar.
🚀 Run from CLI using .tar:
```bash
docker load -i motivation-app.tar
docker run -p 8501:8501 motivation-app
```
🎯 Run from a .bat file (Windows only):

Create a run_app.bat file with this content:
```text
@echo off
echo Loading image...
docker load -i motivation-app.tar

echo Starting the app...
start http://localhost:8501
docker run -p 8501:8501 motivation-app
pause
```

Double-click the .bat file to launch!
7️⃣ How to Check All Docker Images

In any terminal:

```bash
docker images
```

You'll see a list like:

```text
REPOSITORY       TAG       IMAGE ID       CREATED          SIZE
motivation-app   latest    abc123def456   5 minutes ago    722MB
```

🧼 Bonus: Clean Up Unused Images

To remove dangling/unused images:
```bash
docker image prune
```
Or delete a specific image:
```bash
docker rmi motivation-app
```

✅ Final Tips

    Keep your Dockerfile and app structure clean and minimal.

    Avoid absolute paths in your code. Use relative paths or os.path.dirname(__file__).

    Test inside Docker to ensure all resources load correctly.

    Share .tar + .bat for the cleanest, no-code-exposed sharing.

---