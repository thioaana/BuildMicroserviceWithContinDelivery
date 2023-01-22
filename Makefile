install:
		# Install depedencies
		pip install pip --upgrade pip &&\
		pip install -r requirements.txt

format:
		# Formatting code with Black
		black *.py mylib/*.py
lint:
		# lint

test:
		# test

all:
		# install lint test format