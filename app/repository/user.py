from sqlalchemy.orm import Session
from app.db import models
from fastapi import HTTPException,status




def enviar_estudios(estudio,db= Session):
    estudio = estudio.dict()
    try:
        nuevo_usuario = models.Estudios(     
            estudio = estudio["estudio"],
        )
        db.add(nuevo_usuario)
        db.commit()
        db.refresh(nuevo_usuario)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail= f"Error enviando estudio{e}"
        )
def solicitar_estudios(estudio,db=Session):
    estudio = estudio.dict()
    try:
        nuevo_estudio = models.Estudios(
            estudio = estudio["estudio"],
        )
        db.add(nuevo_estudio)
        db.commit()
        db.refresh(nuevo_estudio)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Error solicitando estudio{e}"
        )
# def obtener_estudios(estudio_id,db= Session):
#     usuario = db.query(models.Estudios).filter(models.Estudios.id == id).first()
#     if not usuario:
#         raise HTTPException(
#             status_code= status.HTTP_404_NOT_FOUND,
#             detail= f"No existe el usuario con el id {estudio_id}"
#             )
#     return usuario
def obtener_usuario(db:Session):
    data = db.query(models.Estudios).all()
    return data


def obtener_estudios(db:Session):
    data = db.query(models.Estudios).all()
    return data


