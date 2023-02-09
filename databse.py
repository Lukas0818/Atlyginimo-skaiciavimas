import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///database.db')
Base = declarative_base()

class Duombaze(Base):
    __tablename__ = 'Pinigai'
    id = Column(Integer, primary_key=True)
    vardas = Column("Vardas", String)
    pinigai = Column("Pinigai", Float)
    data = Column("Diena", DateTime, default=datetime.datetime.utcnow)

    def __init__(self, vardas, pinigai):
        self.vardas = vardas
        self.pinigai = pinigai

    def __repr__(self):
        return f"ID: {self.id}, VARDAS: {self.vardas}, Pinigai: {self.pinigai}, Data: {self.data}"

Base.metadata.create_all(engine)