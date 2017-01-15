from models import Base, Column, Integer, String


class User(Base):
    __tablename__ = 'user'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    name = Column('name', String(20))

    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return "<User(id=%s, name='%s')>" % (self.id, self.name)
