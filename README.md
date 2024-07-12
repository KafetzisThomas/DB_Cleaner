<h1 align="center">DB_Cleaner</h1>

__What Is This?__ - Cleans your PostgreSQL db by removing rows with NULL values in specified columns.

__How to Download__: Open the terminal on your machine and type the following command:

```bash
git clone https://github.com/KafetzisThomas/DB_Cleaner.git
```

## Setup

### Set up Virtual Environment

```bash
➜ cd path/to/script/directory
$ python3 -m venv env/
$ source env/bin/activate
```

### Install Dependencies

```bash
$ pip3 install -r requirements.txt
```

### Create Enviroment Variable file

```bash
$ touch .env
$ nano .env
```

Add the following environment variables (modify as needed):
```bash
➜ DB_HOST="example_host"
➜ DB_NAME="example_name"
➜ DB_TABLE="example_table"
➜ DB_COLUMN="example_column"
➜ DB_USER="example_user"
➜ DB_PASSWORD="example_password"
➜ DB_PORT="example_port"
```

Save changes and close the file.

### Run Python Script
```bash
$ python3 main.py
```
