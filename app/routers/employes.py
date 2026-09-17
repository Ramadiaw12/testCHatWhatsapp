from fastapi import APIRouter 


router=APIRouter(prefis="/employees", tags=["Employees"])


@router.get("/")
def get_employees():
    return []