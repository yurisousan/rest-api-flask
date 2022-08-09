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
```bash
pip install flask flask-restful
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
