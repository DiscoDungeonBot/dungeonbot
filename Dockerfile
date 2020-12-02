# Use an official Python runtime as a parent image
# py-roll does not work with python 3.8
FROM python:3.7

# Set the working directory to /app
WORKDIR /app

COPY requirements.txt /app/
# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Copy the current directory contents into the container at /app
COPY main.py /app/
COPY dungeonbot /app/dungeonbot

# Pass in your Discord Key here
ENV DISCORD_TOKEN=''

# Run dice.py when the container launches
CMD ["python", "main.py"]