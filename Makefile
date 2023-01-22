install:
		pip install pip --upgrade pip &&\
		pip install -r requirements.txt
lint:
		# lint
test:
		# test
format:
		# format
all:
		install lint test format