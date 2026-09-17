# FIRST API CLASSIQUE 
from fastapi import FastAPI
from app.routers.employes import router as employees_router

app= FastAPI(title="employee Management API !")
app.include_router(employees_router)


@app.get("/")
def root() :
    return {"messages": "Employes api is running"} 