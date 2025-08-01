FROM python:3.9-slim-buster
COPY requirements.txt .
COPY data_generator.py . 
RUN pip3 install -r requirements.txt
CMD ["python3", "data_generator.py"]
