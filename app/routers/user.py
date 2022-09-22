
from fastapi import APIRouter,Depends,status
from app.schemas import  Estudios, User,ShowUser, UptadeUser
from app.db.database import get_db
from app.db.database_get import get_db2
from sqlalchemy.orm import Session
from typing import List
from app.repository import user 



router = APIRouter(
    prefix="/user",
    tags=["Users"]
)


@router.get("/",response_model= List[Estudios],status_code= status.HTTP_200_OK)
def obtener_estudios(db:Session = Depends(get_db2)):
    data = user.obtener_estudios(db)
    return data


@router.post("/",status_code= status.HTTP_201_CREATED)
def enviar_estudios(usuario:Estudios,db:Session = Depends(get_db)):
    user.enviar_estudios(usuario,db)
    return {"respuesta": "Estudios enviados con exito!!"}


@router.post("/solictar",status_code=status.HTTP_201_CREATED)
def solicitar_estudios(estudios:Estudios,db:Session = Depends(get_db2)):
    user.solicitar_estudios(estudios,db)
    return {"respuesta": "Solicitud enviado"}

@router.get("",response_model= List[Estudios],status_code= status.HTTP_200_OK)
def obtener_estudios(db:Session = Depends(get_db)):
    data = user.obtener_estudios(db)
    return data



 
    

