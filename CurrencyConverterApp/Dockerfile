FROM python:3.9.21-alpine

# Set the working directory in the container
WORKDIR /app

# Install any dependencies specified in requirements.txt
# RUN apt update &&\
  #  apt install -y python3-pip 
RUN pip install flask 
RUN pip install requests
RUN pip install urllib3


# Copy the entire application code to the working directory
COPY . .

# Expose the port the app runs on
EXPOSE 5000

# Set environment variable for Flask
ENV FLASK_APP=app.py

# Run the application
#CMD ["flask", "-m", "run", "--host=0.0.0.0", "--port=5000"]
CMD ["python3", "app.py"]
