from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from . import models, schemas, auth
from .database import engine, Base, get_db

Base.metadata.create_all(bind=engine)

app = FastAPI(title="HR Management API")

@app.post('/auth/register', response_model=schemas.User)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail='Username already registered')
    hashed_password = auth.get_password_hash(user.password)
    new_user = models.User(username=user.username, hashed_password=hashed_password, role=user.role)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.post('/auth/login', response_model=schemas.Token)
def login(form_data: auth.OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    return auth.login_for_access_token(form_data, db)

@app.get('/users/me', response_model=schemas.User)
def read_users_me(current_user: models.User = Depends(auth.get_current_user)):
    return current_user

@app.post('/goals/', response_model=schemas.Goal)
def create_goal(goal: schemas.GoalCreate, db: Session = Depends(get_db), current_user: models.User = Depends(auth.get_current_user)):
    db_goal = models.Goal(**goal.dict(), owner_id=current_user.id)
    db.add(db_goal)
    db.commit()
    db.refresh(db_goal)
    return db_goal

@app.get('/goals/', response_model=list[schemas.Goal])
def read_goals(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), current_user: models.User = Depends(auth.get_current_user)):
    goals = db.query(models.Goal).filter(models.Goal.owner_id == current_user.id).offset(skip).limit(limit).all()
    return goals

@app.get('/admin/users', response_model=list[schemas.User])
def read_users(current_user: models.User = Depends(auth.get_current_active_admin), db: Session = Depends(get_db)):
    return db.query(models.User).all()
