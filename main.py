#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# Project Title: DB_Cleaner (https://github.com/KafetzisThomas/DB_Cleaner)
# Author / Project Owner: KafetzisThomas (https://github.com/KafetzisThomas)

import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_TABLE = os.getenv("DB_TABLE")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = os.getenv("DB_PORT")

connection = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(connection).execution_options(autocommit=True)

df = pd.read_sql_query(f"select * from {DB_TABLE}", con=engine)

# Drop rows with NaN values (NULL)
df.dropna(inplace=True)

# Update data back to the database
df.to_sql(DB_TABLE, con=engine, if_exists="replace", index=False)

print(df.to_string())
