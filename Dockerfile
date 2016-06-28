FROM ubuntu:trusty
MAINTAINER Nick Krichevsky <nick@ollien.com>

RUN apt-get update
RUN apt-get update
RUN apt-get install -y python3-pip
COPY requirements.txt /root/requirements.txt
COPY main.py /root/main.py
RUN pip3 install -r /root/requirements.txt
CMD ["python3", "/root/main.py"]
