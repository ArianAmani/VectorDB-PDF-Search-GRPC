FROM ubuntu:22.04

# Install linux packages
RUN apt-get update && apt-get install -y python3 python3-pip

# Install python dependencies
COPY requirements.txt .
RUN python3 -m pip install --upgrade pip
RUN pip install --no-cache -r requirements.txt

# Create working directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Copy contents
COPY ./app /usr/src/app

# Set environment variables
# ENV HOME=/usr/src/app

CMD ["python3", "./server.py"]

# fteam8
