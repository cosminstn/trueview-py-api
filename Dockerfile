#FROM ubuntu:16.04
#
#MAINTAINER Cosmin Stoian "cosmin.stn1997@gmail.com"
#
#RUN apt-get update -y && \
#    apt-get upgrade -y && \
#    apt-get install -y python-pip python-dev
#
#COPY ./requirements.txt /app/requirements.txt
#
#WORKDIR /app
#
#RUN pip install -r requirements.txt
#
#COPY . /app
#
#ENTRYPOINT ["python"]
#
#CMD ["app.py"]

FROM ubuntu:18.04

MAINTAINER Cosmin Stoian "cosmin.stn1997@gmail.com"

RUN apt-get update
RUN apt-get install -y python3 python3-dev python3-pip

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY . /app

ENTRYPOINT ["./app.py"]

CMD [ "flask", "run", "--host=0.0.0.0" ]