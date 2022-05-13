# FastAPI proj

Originally from [fastapi-sqlmodel-alembic](https://github.com/testdrivenio/fastapi-sqlmodel-alembic) and [fastapi-celery](https://github.com/testdrivenio/fastapi-celery)

FastAPI, Pydantic, async SQLAlchemy, SQLModel, Postgres, Alembic, and Docker.

Celery (with Redis 7)

## TODO:

- add Pytest
- add complex Pydantic models w/ computed props

## Run:

```sh
$ docker-compose up -d --build
$ docker-compose exec web alembic upgrade head
```

Sanity check: [http://localhost:8004/ping](http://localhost:8004/ping)

Add a song:

```sh
$ curl -d '{"name":"Midnight Fit", "artist":"Mogwai", "year":"2021"}' -H "Content-Type: application/json" -X POST http://localhost:8004/songs
```

Get all songs: [http://localhost:8004/songs](http://localhost:8004/songs)
