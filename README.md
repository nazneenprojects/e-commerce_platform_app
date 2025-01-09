# e-commerce_platform_app
e-commerce_platform_app  with Tech Stack  Python3, FastAPI, PostgresSQL Docker, Unit testing, Render


## How to ?
1. To Run the project "poetry run uvicorn app.main:app --reload"
2. To install the poetry project : "poetry init"
3. To add the dependencies : "example, poetry add fastapi uvicorn"
4. To remove the poetry 
    "rm pyproject.toml poetry.lock"
    "poetry env remove python"
5. Alembic Set up:
    a. poetry add alembic
    b. alembic init alembic
    c. update files : env.py and alembic.ini
    d. before running app , generate migration script : alembic revision --autogenerate -m "Initial migration"
    e. apply migration:  alembic upgrade head



