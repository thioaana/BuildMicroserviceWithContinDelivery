install:
		# Install depedencies
		pip install pip --upgrade pip \
		&& pip install -r requirements.txt \
		&& python -m textblob.download_corpora 		# Necessary corpora for textblob nlp

lint:
		pylint --disable=R,C *.py mylib/*.py

test:
		python -m pytest -vv --cov=mylib --cov=main test_*.py

format:
		# Formatting code with Black
		black *.py mylib/*.py

build:
		# build container
		docker build -t deploy-fastapi .

run:
		# run docker
		docker run -p 127.0.0.1:8080:8080 21a38fc9ad66

all:
		# install lint test format