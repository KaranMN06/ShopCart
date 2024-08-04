from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import create_engine, Column, Integer, String
import sqlalchemy
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel
 
# Database setup
#DATABASE_URL = "sqlite:///./test.db"
#DATABASE_URI = 'postgresql://postgres:<password>@localhost/<name_of_the_datbase>'
db_name="testdb"
db_user="postgres"
db_passwd="Admin%40123"
db_host="localhost"
db_port="5432"

DATABASE_URL=f"postgresql://postgres:{db_passwd}@localhost:5432/testdb"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = sqlalchemy.orm.declarative_base()




# Dependency to get the database session
def get_db():
	db = SessionLocal()
	try:
		yield db
	finally:
		db.close()
