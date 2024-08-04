from fastapi import FastAPI,Depends
from fastapi import APIRouter
from schemas import AdminCreate,AdminLogin
from fastapi.encoders import jsonable_encoder
import hashlib
from database import Base,engine,get_db
from models import Adminsignup,Adminlogin
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel
import sqlalchemy as d

admin_cred=APIRouter()


Base.metadata.create_all(bind=engine)


key_hash=hashlib.new("SHA256")

@admin_cred.post("/admin-signup/")
async def admin_signup(admin:AdminCreate, db: Session = Depends(get_db)):
    key_hash.update(str(admin.password).encode() ) 
    hashed_password = key_hash.hexdigest()
    print("Hash:", hashed_password)  
    admin_data = Adminsignup(username=admin.username, password=hashed_password)
    print()
    db.add(admin_data)
    db.commit()
    db.refresh(admin_data)
    
    data = jsonable_encoder(admin)

    return data

@admin_cred.post("/admin-login/")
async def admin_login(admin:AdminLogin, db: Session = Depends(get_db)): 
    user = db.query(Adminsignup).filter(Adminsignup.username == admin.username).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    key_hash = hashlib.new("SHA256")
    key_hash.update(str(admin.password).encode())
    hashed_password = key_hash.hexdigest()
    if user.password != hashed_password:
        raise HTTPException(status_code=401, detail={"message": "Incorrect password"})
    
    admin_data = Adminlogin(username=admin.username, password=hashed_password)
    db.add(admin_data)
    db.commit()
    db.refresh(admin_data)
    return {"message": "Login successful"}



# @admin_cred.post("/admin-signup/")
# async def admin_signup(admin:AdminCreate,db: Session = Depends(get_db)):
#     bytes = str(admin.passwrord).encode('utf-8') 
#     salt = bcrypt.gensalt() 
#     hash = bcrypt.hashpw(bytes, salt)
#     print(type(hash))
#     admin_data = Adminsignup(username=admin.username,password=hash)
#     db.add(admin_data)
#     db.commit()
#     db.refresh(admin_data)
    
#     data=jsonable_encoder(admin)
   
#     return data

# @admin_cred.post("/admin-login/")
# async def admin_login(admin:AdminLogin,db: Session = Depends(get_db)): 
#     admin_login_data = str(admin.passwrord).encode('utf-8') 
#     print(admin_login_data)
#     hashed_pass = db.query(Adminsignup).filter(Adminsignup.id == admin.id).first().password.encode('utf-8')
#     print(hashed_pass)
#     result = bcrypt.checkpw(admin_login_data, hashed_pass)
#     if result:
#         admin_data=Adminlogin(username=admin.username,password=hash)
#         db.add(admin_data)
#         db.commit()
#         db.refresh(admin_data)
#         return "u have logged in"
        
#     else:
#         return "wrong username or password"
    
    
    
#     # user = db.query(Adminsignup).filter(Admin.id == user_id).first()
#     # admin_data=Adminlogin(username=admin.username,password=hash)
#     # db.add(admin_data)
#     # db.commit()
#     # db.refresh(admin_data)
#     # return admin_data

'''hash and unhash password '''
# import bcrypt

# # Hashing a password
# def hash_password(password):
#     # Generate a salt and hash the password
#     salt = bcrypt.gensalt()
#     hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
#     return hashed_password

# # Verifying a password
# def verify_password(stored_hash, password):
#     # Check if the provided password matches the stored hash
#     return bcrypt.checkpw(password.encode('utf-8'), stored_hash)

# # Example usage
# password = "my_secure_password"
# hashed = hash_password(password)
# print(f"Hashed password: {hashed}")

# # Verification
# is_correct = verify_password(hashed, password)
# print(f"Password is correct: {is_correct}")
