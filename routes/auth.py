from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel
import uuid
import bcrypt
from models.user import User
from pydantic_schema.user_create import UserCreate
from fastapi import APIRouter
from database import db 

router=APIRouter()

@router.post('/signup')
def signup_user(user : UserCreate):
    
    user_db=db.query(User).filter(User.email == user.email).first()

    if user_db:
        raise HTTPException(400,"user with the same email already exist")
    

    hashed_pw=bcrypt.hashpw(user.password.encode(),bcrypt.gensalt())
    
    user_db=User(id=str(uuid.uuid4()),email=user.email,password=hashed_pw,name=user.name)
    
    db.add(user_db)
    db.commit() 
    db.refresh(user_db)

    return user_db
