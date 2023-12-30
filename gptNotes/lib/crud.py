import datetime
from typing import Any

from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import Session
from flask import abort

from . import models


class RepositoryBase:
    def __init__(self, db: Session, model_class: object, default_id_field: str | None = "id"):
        if default_id_field is not None:
            assert hasattr(model_class, default_id_field)

        self._db = db
        self._model_class = model_class
        self._default_id_field = default_id_field

    def get_all(self):
        '''
        get all rows
        '''

        return self._db.query(self._model_class).all()
    
    def get_one(self, id: Any, id_field: str | None = None):
        '''
        get one row with given id (by id_field)
        '''

        id_field = id_field or self._default_id_field
        assert hasattr(self._model_class, id_field)

        return self._db.query(self._model_class).filter(getattr(self._model_class, id_field) == id).first()

    def check_exists(self, id: Any, id_field: str | None = None):
        '''
        check if row with given id (by id_field) exists
        '''

        id_field = id_field or self._default_id_field
        assert hasattr(self._model_class, id_field)

        return self._db.query(self._model_class).filter(getattr(self._model_class, id_field) == id).count() > 0

    def delete_one(self, id: Any, id_field: str | None = None):
        '''
        delete one row with given id (by id_field)
        '''

        id_field = id_field or self._default_id_field
        assert hasattr(self._model_class, id_field)

        try:
            deleted_count = self._db.query(self._model_class).filter(getattr(self._model_class, id_field) == id).delete()
            self._db.commit()
        except:
            return 0

        return deleted_count

    def add_one(self, model: Any):
        '''
        add one row (by model) to db
        '''

        assert type(model) == self._model_class

        self._db.add(model)
        self._db.commit()
        self._db.refresh(model)

        return model


class UserRepository(RepositoryBase):
    def __init__(self, db: Session):
        super().__init__(db, models.User)
    
    def create_one(self, username, password):
        if self.check_exists(username, id_field='username'):
            abort(400)
        
        db_user = models.User(
            username=username,
            password=generate_password_hash(password),
        )

        return self.add_one(db_user)
    
    def check_password(self, username, password):
        if not self.check_exists(username, id_field='username'):
            abort(400)
        
        db_user = self.get_one(username, id_field='username')

        return check_password_hash(db_user.password, password)


class NoteRepository(RepositoryBase):
    def __init__(self, db: Session):
        super().__init__(db, models.Note)

    def create_one(self, user_id, title, text):
        user_repository = UserRepository(self._db)
        if not user_repository.check_exists(user_id):
            abort(400)
        
        db_note = models.Note(
            create_time=datetime.datetime.now(),
            user_id=user_id,
            title=title,
            text=text,
        )

        return self.add_one(db_note)
