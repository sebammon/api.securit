# securIT

## Setup
1. Create a virtualenv
1. Install python version >= 3.4.0 and supporting pip version
2. If you are on Raspberry Pi run `pip install RPi.GPIO` otherwise run `pip install fake-rpi`
3. Install virtualenv with `pip install virtualenv`
4. Create virtualenv
5. Active virtualenv
6. Install dependencies with `pip install -r requirements.txt`

## Running the server
1. Navigate to project's source directory
2. Activate virtualenv
3. Run `python run.py`

## Deployment
According to this [article](https://medium.com/ymedialabs-innovation/deploy-flask-app-with-nginx-using-gunicorn-and-supervisor-d7a93aa07c18).

* NGINX
* Gunicorn
* Supervisor