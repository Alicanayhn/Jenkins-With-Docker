FROM python:3.10
WORKDIR /Web
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD [ "python", "app.py"]