# flask-docker-hello-world


This is creating a Flask App docker image that can do simple things.
Eventually this will be extended to handle having pickled models placed in them and then used to predict when data
is input

### a docker compose command
```bash
docker-compose up
#this will build the flask App
```

### a docker compose command
```bash
docker-compose exec web python make-request.py
#this is the command for the routes within the flask app
```
