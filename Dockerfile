# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory to /app
WORKDIR /app

COPY requirements.txt /app/
# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Copy the current directory contents into the container at /app
COPY main.py /app/
COPY dungeonbot /app/dungeonbot

# Make Prometheus port 8000 available to the world outside this container
EXPOSE 8000

# Pass in your Discord Key here
ENV DISCORD_TOKEN=''

# Run dice.py when the container launches
CMD ["python", "main.py"]