FROM python
LABEL maintainer="ryangroden@gmail.com"


COPY ./requirements.txt /src/requirements.txt

COPY ./test /test
WORKDIR /src

RUN pip install -r requirements.txt

COPY ./src /src
 


# Run the program by starting flask
ENTRYPOINT ["python"]
CMD ["app.py"]
