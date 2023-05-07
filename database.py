from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine.url import URL
import cx_Oracle

cx_Oracle.init_oracle_client(lib_dir=r"C:\Oracle\instantclient")

connect_url = "oracle+cx_oracle://system:admin@localhost:1521/xe"

engine = create_engine(connect_url, max_identifier_length=128)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
