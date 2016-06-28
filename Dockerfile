FROM ubuntu:trusty
MAINTAINER Nick Krichevsky <nick@ollien.com>

RUN apt-add-repository ppa:fkrull/deadsnakes
RUN apt-get update
RUN apt-get install -y python3.5 python3-pip
COPY requirements.txt
COPY main.py
RUN pip install -r requirements.txt
CMD ["python3 main.py"]
