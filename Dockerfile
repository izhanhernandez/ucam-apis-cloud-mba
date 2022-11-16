FROM python:3.8.10-slim

# Define Locale parameters
ENV LC_ALL=en_US.UTF-8
ENV LANG=en_US.UTF-8
ENV LANGUAGE=en_US.UTF-8
ENV PYTHONIOENCODING=utf-8

# Install basic dependencies
RUN apt -y update
RUN apt -y upgrade
RUN apt -y install curl
RUN apt -y install wget
RUN apt -y install python3-pip
RUN apt -y install iputils-ping

# Copy the files to the App folder
COPY . /App

# Define Working dir
WORKDIR /App

# Install the python requirements
RUN pip install -r requirements.txt

# Define the CMD
ENTRYPOINT ["python3"]
CMD ["/App/ApiCalculadora.py"]