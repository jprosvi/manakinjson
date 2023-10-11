FROM registry.access.redhat.com/ubi9/python-311

WORKDIR /app
COPY . .
RUN pip3 install -r requirements.txt

USER 1001
CMD python3 app.py
