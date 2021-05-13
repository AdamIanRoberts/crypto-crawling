from sqlalchemy import Column, Float, JSON, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.declarative.api import DeclarativeMeta


Base: DeclarativeMeta = declarative_base()


class Trades(Base):
    __tablename__ = "trades"

    format = Column(String, nullable=True)
    timestamp = Column(String, nullable=False, index=True, primary_key=True)
    receipt_timestamp = Column(String, nullable=False, index=True)
    feed = Column(String, nullable=False, index=True)
    symbol = Column(String, nullable=False, index=True)
    side = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    price = Column(Float, nullable=False)
    id = Column(String, nullable=True)
    order_type = Column(String, nullable=True)

    def __repr__(self):
        class_name = self.__class__.__name__
        return f"{class_name}({self.symbol}, {self.timestamp})"


class Book(Base):
    __tablename__ = "book"

    format = Column(String, nullable=True)
    timestamp = Column(String, nullable=False, index=True, primary_key=True)
    receipt_timestamp = Column(String, nullable=False, index=True)
    feed = Column(String, nullable=False, index=True)
    symbol = Column(String, nullable=False, index=True)
    data = Column(JSON, nullable=False)

    def __repr__(self):
        class_name = self.__class__.__name__
        return f"{class_name}({self.symbol}, {self.timestamp})"
