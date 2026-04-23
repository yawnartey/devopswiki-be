# base image
FROM python:3.12-slim

# working directory
WORKDIR /app

# copy requirements to working directory and and install it
COPY requirement.txt .
RUN pip install -r requirement.txt

# copy application code to the working directory
COPY . .

# set right permission on entrypoint script
RUN chmod +x entrypoint.sh

# expose the port the application will run on
EXPOSE 8000

# run the fastapi application
CMD ["./entrypoint.sh"]