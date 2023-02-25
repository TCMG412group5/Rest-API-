# A dockerfile must always start by importing the base image.
# So we write 'python' for the image name and 'latest' for the version.
FROM python:latest

# Here we put the file at the image root folder.
COPY Flask.py /
RUN pip install Flask
RUN pip install requests

# We need to define the command to launch when we are going to run the image.
CMD [ "python3", "./Flask.py" ]
