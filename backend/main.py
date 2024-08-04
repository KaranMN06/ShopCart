from fastapi import FastAPI
from signup import admin_cred

app=FastAPI(title="ShopCart")

app.include_router(admin_cred)
