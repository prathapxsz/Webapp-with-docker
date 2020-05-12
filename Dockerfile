FROM ubuntu
RUN apt-get -y update && apt-get -y install python3 python3-pip python-dev sqlite3
ADD . /webapp
WORKDIR /webapp/app
RUN pip3 install -r requirements.txt
EXPOSE 5000
CMD python3 app.py


