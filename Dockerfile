FROM ubuntu:trusty
MAINTAINER Nick Krichevsky <nick@ollien.com>

RUN apt-get update
RUN apt-get install -y software-properties-common
RUN add-apt-repository ppa:fkrull/deadsnakes
RUN apt-get update
RUN apt-get install -y python3.5 python3-pip
COPY requirements.txt ~/requirements.txt
COPY main.py ~/main.py
RUN cd ~/
RUN pip install -r requirements.txt
CMD ["python3 main.py"]
