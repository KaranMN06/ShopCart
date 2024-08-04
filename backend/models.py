from sqlalchemy import create_engine, Column, Integer, String,DateTime,func
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel
from database import Base
from datetime import datetime



# Database model
class Adminsignup(Base):
	__tablename__ = "adminSignup"
	id = Column(Integer, primary_key=True, index=True)
	username = Column(String)
	password = Column(String,index=True)
	
 
class Adminlogin(Base):
	__tablename__ = "adminLogin"
	id = Column(Integer, primary_key=True, index=True)
	username = Column(String)
	password = Column(String,index=True)
	logintime =  Column(DateTime, default=func.now())

