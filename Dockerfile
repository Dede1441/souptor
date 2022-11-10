FROM python:latest
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
COPY snmp_interrogate.py snmp_interrogate.py
CMD [ "python3", "snmp_interrogate.py"]