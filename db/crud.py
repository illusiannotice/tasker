from task_end.task_struct import Task
from sqlalchemy import create_engine, insert, delete
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
from db.tables import TaskTable, Base
from task_end.crud import create_task
from os import environ
from dotenv import load_dotenv
from pathlib import Path


load_dotenv()
db_url: str = environ["DB_URL"]
engine = create_engine(db_url)
Session = sessionmaker(bind=engine)
session = Session()
if not database_exists(engine.url):
    create_database(engine.url)
Base.metadata.create_all(bind=engine)

def add_task_db(task: Task):
    with engine.connect() as conn:
        conn.execute(insert(TaskTable).values(create_task(task)))
        conn.commit()
def read_all():
    row = session.query(TaskTable)
    task_list = []
    for task in row:
        task_list.append(task.make_dict())
    return task_list

def delete_task(task_name: str):
    with engine.connect() as conn:
        conn.execute(delete(TaskTable).where(TaskTable.label == task_name))
        conn.commit()
