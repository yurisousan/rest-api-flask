# rest-api-flask

# Requirements
```bash
sudo apt install python3-pip python3-virtualenv python3-venv
```

# Initial
Create a venv
```bash
python3 -m venv .venv
```

### Using the Virtual Environment
```bash
source .venv/bin/activate
```

### Install packages
[FlaskMongoEngine Doc](http://docs.mongoengine.org/projects/flask-mongoengine/en/latest/)

```bash
pip install flask flask-restful flask-mongoengine
```

Verify libs from ```venv```
```bash
pip freeze

pip freeze > requirements.txt
```

### Simple application
[Flask Documentation](https://flask.palletsprojects.com/en/2.2.x/quickstart/#a-minimal-application)

[Flask Restful Documentation](https://flask-restful.readthedocs.io/en/latest/quickstart.html#a-minimal-api)

```bash
flask run # to flask

python app.py # to restful
```

## Tests
[Reffer Documentation](https://peps.python.org/pep-0008/)

Install the lib
```bash
sudp pip install flake8
```

Using

```bash
flake8 . --exclude .venv
```

Now remove the infos that it return to solve, and push again to repository.


# TShoot
Access the mongodb container

```bash
docker exec -it id-container sh

mongo -u admin

> show dbs

> use admin

> show collections

> exit
```