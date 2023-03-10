[![Python application test with Github Actions](https://github.com/thioaana/BuildMicroserviceWithContinDelivery/actions/workflows/devops.yml/badge.svg)](https://github.com/thioaana/BuildMicroserviceWithContinDelivery/actions/workflows/devops.yml)

## Process to Build a Python Microservice with Continues Delivery

**Steps to follow**
1. Setup virtual environmnt 
    - In CLI virtualenv ~/.venv
    - Insert source ~/.venv/bin/activate in ~/.bashrc
2. Scaffolding the structure of the project, creating the appropriate empty files
    - Makefile
    - Dockerfile
    - requiremnts.txt
    - main.py 
    - Directory with libraries and inside __init__.py, logic.py
    - test_logic.py
3. Fill only Install recipe in Makefile. Let the rest with  comments
4. Fill requirements.txt
    - Insert the dependencies-packages
    - Run make install
    - Run pip freeze to find the version of each package
    - Complete requirements.txt with versions
5. Setup Github Actions
    - Actions -> Python application ... -> Create yml, name it and commit commenting "Start Continuous Integration"
    - Actions -> click Start Cont.... Few sec to build.
    - Actions -> click 3dots (upper right) -> Create Budge -> Copy the code
    - Paste it on the top of Readme.
6. Formatting code with Python Black
    - Fill format in Makefile eg black *.py
    - Write sample of code in py files.
    - Run make format
    - Fill yml
    - Push and Build to be verified
7. Lint 
    - Fill format in Makefile eg pylint
    - Run make format
    - Fill yml
    - Push and Build to be verified
8. Build a cli tool using Python fire utility to test from prompt
    - Create a python fily eg cli_fire.py
    - Execute it from cl with the relevant parameters.
9. Create the web microservice api using Fastapi based on logic.py
    - Two simple functions using wiki and search_wiki
    - One more function using textblobnlp for nlp. Before executing we should download corpora with python -m textblob.download_corpora 
10.Build docker
    - Fill the build:recipe in Makefile with "docker build -t deploy-fastapi ."
    - Fill Dockerfile
    - Run make build
    - Execute "docker image ls" and copy the image number
    - Fill the run:recipe in Makefile with "docker run -p 127.0.0.1:8080:8080 2cfc26d51635". The last code is that copied before.