FROM python:3.9-slim

ENV FLASK_APP app/runner/run.py
ENV PIP_ROOT_USER_ACTION ignore

# Copy local code to the container image
COPY . ./

RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt

# Run the web service on container startup. Here we use the gunicorn
# webserver, with one worker process and 8 threads.
# For environments with multiple CPU cores, increase the number of workers
# to be equal to the cores available.
# Timeout is set to 0 to disable the timeouts of the workers to allow Cloud Run to handle instance scaling.
EXPOSE 8080
ENV PORT 8080
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 app.runner.run:app