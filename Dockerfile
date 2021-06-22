FROM ubuntu
LABEL maintainer="ryangroden@gmail.com"

RUN apt-get update -y && apt-get install -y python3-pip python3-dev

EXPOSE 9999/tcp

COPY ./requirements.txt /src/requirements.txt

WORKDIR /src

RUN pip3 install -r requirements.txt

COPY ./src /src
 


# Run the program by starting flask
ENTRYPOINT ["python3"]
CMD ["app.py"]
