install:
		# Install depedencies
		pip install pip --upgrade pip &&\
		pip install -r requirements.txt 
		# python -m textblob.download_corpora 

lint:
		pylint --disable=R,C *.py mylib/*.py

test:
		python -m pytest -vv --cov=mylib --cov=main test_*.py

format:
		# Formatting code with Black
		black *.py mylib/*.py

all:
		# install lint test format