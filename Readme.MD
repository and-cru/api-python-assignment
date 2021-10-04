# Patient API

> CRUD API to schedule and manage appointments

We are building an API with [FastAPI](https://fastapi.tiangolo.com/)

## How it works

All you need is a running [Docker](https://docs.docker.com/get-docker/) daemon. Then simply run the below in the root directory:

```bash
docker-compose up -d --build
```

This will build and bring up the services for the CRUD API. Confirm that the app is up by accessing:

`http://localhost:8080/health` -> Returns an I am healthy message

Access the docs for the API by going to `http://localhost:8080/docs`

## Migrations

> This is optional we can also allow the ORM to create the tables and relationships... but BONUS points here!

Using [alembic](https://alembic.sqlalchemy.org/en/latest/tutorial.html#the-migration-environment), we can easily run DB migrations. To run a new migration follow the below:

Navigate into `src`

```bash
cd src/
```

Then run Alembic revision command:

```bash
alembic revision -m 'My new migration'
```

This will generate a new migration file inside the `patient/version`, edit this file and added the DB changes.

For the changes to take effect, run:

```bash
cd .. && docker-compose down && docker-compose up -d --build
```

## Connect to pgAdmin4

> If you want to have a look into the DB and tables itself.... very cool!

To view the DB, open [Chrome](https://www.pgadmin.org/faq/) as limited browsers are supported, then navigate to `localhost:16543/` and login with `username: admin@admin.com` & `password: test123!`

Thereafter click on server -> create new server. Give the server a `name`, to find the hostname run:

```bash
ifconfig |grep inet
```

There will be an IP for our Docker network. The rest is simple... create a new DB server with the Docker IP as hostname, DB username and password is both `postgres`

## To-do:

The assignment is a simple appointment service, we are creating an appointment service for a medical Doctors' practice. We need to load patients into the system and schedule appointments for them. Feel free to use creativity here with the DB models.

Some important constraints to note, appointments are not allowed to be at conflicting times (aka double booking). Inside the `api/` folder there is a `models.py` file containing a barebone example which for models feel free to add DB models here, `schemas.py` is a file containing the schemas (no need to tinker or change here)... lastly, the `crud.py` file is normally where the business logic is housed that is exposed by the endpoints.

Inside the `app/` directory there is a `main.py` file which houses all the endpoints with some barebones examples as well... just to ensure a running start! As a guide, below is a list of items to keep track of implementing.

> Basic functionality

- [ ] Create a patient
- [ ] Read all patients
- [ ] Read a patient
- [ ] Delete a patient
- [ ] Create a appointment
- [ ] Read all appointments
- [ ] Read an appointment for a patient
- [ ] Delete an appointment for a patient

> Bonus

For this section the `schemas.py` file needs some tweaks :)

- [ ] Update a patient
- [ ] Update an appointment - [Pydantic](https://pydantic-docs.helpmanual.io/usage/exporting_models/#modeljson)