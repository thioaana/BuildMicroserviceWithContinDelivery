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
