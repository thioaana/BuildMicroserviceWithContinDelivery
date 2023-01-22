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
    - test.py
3. Fill install recipe in Makefile
4. Fill requirements.txt
    - write the packages
    - run make install
    - run pip freeze to find the version of each package
    - complete requirements.txt with versions
