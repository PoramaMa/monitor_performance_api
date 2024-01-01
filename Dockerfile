# FROM python:3.10.5
FROM python:3.9.13
COPY . /app
WORKDIR /app
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

RUN echo Asia/Bangkok > /etc/timezone

RUN apt-get update && apt-get install -y tzdata

RUN rm /etc/localtime

RUN ln -s /usr/share/zoneinfo/Asia/Bangkok /etc/localtime

#dpkg-reconfigure tzdata
RUN dpkg-reconfigure -f noninteractive tzdata

ENTRYPOINT [ "python3" ]
EXPOSE 5000
CMD ["app.py"]