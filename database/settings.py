import os

DATABASE = {
    'drivername': 'postgresql+psycopg2',
    'host': os.environ['POSTGRES_HOST'],
    'port': os.environ['POSTGRES_PORT'],
    'username': os.environ['USER'],
    'password': os.environ['PASSWORD'],
    'database': 'itrace'
}