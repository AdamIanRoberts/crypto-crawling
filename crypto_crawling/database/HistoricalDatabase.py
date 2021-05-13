from datetime import datetime

import pandas as pd

from sqlalchemy.engine.base import Engine
from sqlalchemy.orm import sessionmaker

from crypto_crawling.database.PostgresEngine import PostgresEngine
from crypto_crawling.database.models import Base, Book, Trades


class HistoricalDatabase:
    def __init__(self, engine: Engine = None) -> None:
        self.engine = engine or PostgresEngine().engine
        self.session_maker = sessionmaker(bind=self.engine)
        Base.metadata.create_all(bind=self.engine)

    def get_books(self, start_date: datetime, end_date: datetime, exchange: str, symbol: str) -> pd.DataFrame:
        session = self.session_maker()
        snapshots = (
            session.query(Book)
            .filter(Book.feed == exchange)
            .filter(Book.symbol == symbol)
            .filter(Book.timestamp.between(start_date, end_date))
            .order_by(Book.timestamp.asc())
            .all()
        )
        session.close()
        snapshots_dict = [s.__dict__ for s in snapshots]
        if len(snapshots_dict) > 0:
            return pd.DataFrame(snapshots_dict).drop(columns=["_sa_instance_state"])
        else:
            return pd.DataFrame()

    def get_trades(self, start_date: datetime, end_date: datetime, exchange: str, symbol: str) -> pd.DataFrame:
        session = self.session_maker()
        snapshots = (
            session.query(Trades)
            .filter(Trades.feed == exchange)
            .filter(Trades.symbol == symbol)
            .filter(Trades.timestamp.between(start_date, end_date))
            .order_by(Trades.timestamp.asc())
            .all()
        )
        session.close()
        snapshots_dict = [s.__dict__ for s in snapshots]
        if len(snapshots_dict) > 0:
            return pd.DataFrame(snapshots_dict).drop(columns=["_sa_instance_state"])
        else:
            return pd.DataFrame()
