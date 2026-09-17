# FIRST API CLASSIQUE 
from fastapi import FastAPI

app= FastAPI(title="employee Management API !")

@app.get("/")
def root() :
    return {"messages": "Employes api is running"} 