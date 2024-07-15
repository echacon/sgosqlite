# declarative_base.py
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker
class Base(DeclarativeBase):
    pass
#C:\Users\echac\Documents\trabajos\Desarrollos\sgosqlite>
#engine = sqlalchemy.create_engine("mariadb+mariadbconnector://ussgo:usuario_sgo_@127.0.0.1:3306/bdsgo")
engine = create_engine("sqlite:///C:\\Users\\echac\\Documents\\trabajos\\Desarrollos\\sgosqlite\\bdsgo.db")
