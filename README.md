# securIT API
This repository serves as the backend (API) for the securIT project.
The securIT project enables Raspberry PIs to be used for home security.
This is achieved by connecting existing or new door contacts as well PIRs to the GPIOs of the Raspberry PI.

## Getting started
To get a local copy and running follow these steps.

### Prerequisites
We assume the following prerequisites.

#### Hardware
* Raspberry Pi
* Door contacts
* PIRs

#### Software
* Python version >= 3.4.0


### Setup
1. Create and activate your virtualenv
2. If you are on Raspberry Pi run `pip install RPi.GPIO` otherwise run `pip install fake-rpi`
3. Install remaining dependencies with `pip install -r requirements.txt`

## Running the server
1. Navigate to project's source directory
2. Activate virtualenv
3. Run `python run.py`

## Deployment
According to this [article](https://medium.com/ymedialabs-innovation/deploy-flask-app-with-nginx-using-gunicorn-and-supervisor-d7a93aa07c18).

* NGINX
* Gunicorn
* Supervisor

## Built with
* Python
* Flask
* RPi.GPIO