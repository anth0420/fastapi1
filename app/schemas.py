from typing import Union
from datetime import datetime
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

#USer Model 
class User(BaseModel):
    username: str
    password: str
    nombre: str
    apellido:str
    direccion: Optional[str]
    correo: str
    telefono: int
    creacion:datetime = datetime.now()
#User uptade Model
class UptadeUser(BaseModel):
    username: str = None
    password: str = None
    nombre: str = None
    apellido:str = None
    direccion: str = None
    correo: str = None 
    telefono: int = None
    
class ShowUser(BaseModel):
    username: str
    nombre: str
    correo: str
    class Config():
        orm_mode = True

class Login(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Union[str, None] = None
    correo: Union[str,None] = None