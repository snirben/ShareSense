# ShareSense
##1.
### Docker
#### run the following command to run DB
docker-compose -p sharesense -f docker/docker-compose-dev.yml up -d

## 2. 
###Sensors
#### run the following command
python3 fireSensor/fireapp.py

## 3.
### API Server
python3 manage.py makemigrations
python3 manage.py migrate
python3 runserver

## 4.
### FrontEnd
#### enter frontend directory
yarn start
