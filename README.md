# Places API

This portion of the app serves data from the [populartimes library](https://github.com/m-wrzr/populartimes/blob/master/README.md) from a simple Flask API.

### Development

1. install dependencies

`pip install -r requirements.txt`

1. activate virtual environment

`source venv/bin/activate`

1. define a `.env` file based on `.env.sample`
1. run the app

`PYTHONPATH=venv/src/populartimes flask run`
