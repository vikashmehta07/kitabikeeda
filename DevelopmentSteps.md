# Kitabi Keeda - Development Steps

## Pre-Requisites

### Download and install
1. Python
2. Git
3. Visual Studio Code (or any other editor/IDE of your choice)

### Project Setup
1. Create a new repository on GitHub
2. Add collaborators if required
3. Clone the repository to your local machine
4. Create and activate a virtual environment
5. Install Django
6. Create a new Django project
7. Create a new Django app

#### Commit - Setup Project

### Further Steps
1. Install python-dotenv
2. Setup environment variables `SECRET_KEY` and `DEBUG` in `.env` file
3. Update `settings.py` to use environment variables
4. Change timezone to `Asia/Kolkata`

#### Commit - Add initial Django app strucutre and environment variables

#### Commit - Update settings.py to use environment variables

#### Commit - Add custom and third-party apps to settings and create VectorStore model

### App - keeda

1. Create a new model `Assistants`
2. Create helper functions to interact with the openai API
3. 