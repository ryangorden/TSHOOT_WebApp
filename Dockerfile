# Begin with a minimal Alpine Linux Python 37.3 container, which is the 
# same version we used for our development

FROM python:3.7.3-alpine
LABEL maintainer="ryangroden@gmail.com"

# Shell commands to execute after basic python 3.7 container
# is deployed. We install requirements from file
#RUN pip install netmiko
#RUN pip install napalm
RUN pip install flask
# Change into the correct directory. WORKDIR is the Docker best practice
# verus "RUN" cd/<name of app dir> as it is cleaner and more explicit
# Uncomment line below if needed
# WORKDIR /src

# Flakh default HTTP port is 5000 I change mine to 9999 in my app. This doesn't actually
# publiclly expose the port but server as a useful reference
EXPOSE 9999/tcp

# Run the program by starting flask
ENTRYPOINT ["python"]
CMD ["app.py"]
