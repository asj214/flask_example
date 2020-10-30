from extensions import db
from sqlalchemy.orm import relationship


# Alias common SQLAlchemy names
Column = db.Column
relationship = relationship
Model = db.Model

class BaseModel(object):

    __table_args__ = {'extend_existing': True}

    created_at = Column(db.DateTime, default=db.func.now())
    updated_at = Column(db.DateTime, default=db.func.now())
    deleted_at = Column(db.DateTime)