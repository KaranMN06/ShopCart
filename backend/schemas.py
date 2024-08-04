from pydantic import BaseModel,Field
from datetime import datetime, time, timedelta


class AdminCreate(BaseModel):
    username:str=Field(max_length=8)
    password:str=Field(max_length=8)
    
class AdminLogin(BaseModel):
    username:str=Field(max_length=8)
    password:str=Field(max_length=8)