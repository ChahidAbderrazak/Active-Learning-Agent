# object-detection

Example of object detection used for fish health monitoring

### TODO List:

- [ ] build the Docker-based image
- [ ] build the dataset
- [ ] train the model
- [ ] deploy the trained model on Jetson

# I. Configuration file

First of all, please create the configuration file named `.env>` in the project folder using the following template

```
PROJECT_NAME=deep-learning
VERSION=v1

#### -----------    DATA-SCIENCE APP/WEB-SERVER  -----------
APP_IMG_BUILDER=dashboard-backend
PYTHON_VERSION=python:3.8
APP_CNTNR_NAME=datascience
APP_SERVER_PORT=8080
APP_HOST_PORT=8080



```

# II. Docker setup instructions

The project can run on Docker using the two following setups:

1. Setup the Docker environment

```
$ ./bash/1-build.sh
```

2. Run the data Science pipeline & jetson-inference containers

```
$ ./bash/3-run.sh
```

3. Get/Open the Web-server URL

```
$ ./bash/4-open-app-servers-in-browser.sh
```

4 . Stop the running docker containers

```
$ ./bash/5-stop-servers.sh
```
