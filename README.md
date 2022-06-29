# ShareSense

## preinstall

1) Docker
2) NodeJs
3) Python
4) Download this file into fireSensor folder:
https://drive.google.com/file/d/1H40XrtmyRacmrFJq1UV-fnYclg_e76Be/view?usp=sharing

## 1.
### Docker
#### run the following command to run DB
```docker-compose -p sharesense -f docker/docker-compose-dev.yml up -d```

## 2. 
### Sensors
#### run the following command
```pip3 install -r requirements```
```python3 fireSensor/fireapp.py```

## 3.
### API Server
```python3 manage.py makemigrations```
```python3 manage.py migrate```
```python3 runserver```

## 4.
### FrontEnd
#### enter frontend directory
```yarn start```
browse to the address which exposed
