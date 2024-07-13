#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# Project Title: DB_Cleaner (https://github.com/KafetzisThomas/DB_Cleaner)
# Author / Project Owner: KafetzisThomas (https://github.com/KafetzisThomas)

import os
from sqlalchemy import create_engine, Table, MetaData, delete
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_TABLE = os.getenv("DB_TABLE")
DB_COLUMN = os.getenv("DB_COLUMN")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = os.getenv("DB_PORT")

connection = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(connection)
metadata = MetaData()
metadata.reflect(bind=engine)
table = Table(DB_TABLE, metadata, autoload=True, autoload_with=engine)

# Create a delete statement to remove rows where column is null (None)
delete_stmt = delete(table).where(table.c[DB_COLUMN].is_(None))

with engine.connect() as connection:
    result = connection.execute(delete_stmt)
    connection.commit()
    print(f"Deleted {result.rowcount} rows from {DB_TABLE} where {DB_COLUMN} was NULL.")

print("Database table cleanup completed.")
