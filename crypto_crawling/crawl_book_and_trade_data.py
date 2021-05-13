import argparse
import logging
import os
from typing import List, Dict

from cryptofeed import FeedHandler
from cryptofeed.backends.postgres import BookDeltaPostgres, BookPostgres, TradePostgres
from cryptofeed.defines import BOOK_DELTA, L2_BOOK, TRADES
from cryptofeed.exchanges import EXCHANGE_MAP

from crypto_crawling.env import setup_environment_variables


def parse_arguments():
    parser = argparse.ArgumentParser(description="Start crawling book and trade data.")
    parser.add_argument(
        "--symbols",
        help="List of symbols to download (e.g. [BTC-USDT]).",
        default=["BTC-USDT"],
    )
    parser.add_argument(
        "--exchanges",
        help="List of exchanges to download from (e.g. [BINANCE]).",
        default=["BINANCE"],
    )
    return parser.parse_args()


def get_postgres_cfg_details() -> Dict[str, str]:
    setup_environment_variables()
    return {
        "host": os.environ["POSTGRES_HOST"],
        "user": os.environ["POSTGRES_USER"],
        "db": os.environ["POSTGRES_DB"],
        "pw": os.environ["POSTGRES_PASSWORD"],
        "port": os.environ["POSTGRES_PORT"],
    }


def crawl_book_and_trade_data(symbols: List[str], exchanges: List[str]) -> None:
    postgres_cfg = get_postgres_cfg_details()
    feed_handler = FeedHandler()
    for exchange in exchanges:
        feed_handler.add_feed(
            EXCHANGE_MAP[exchange](
                channels=[L2_BOOK, TRADES],
                symbols=symbols,
                callbacks={
                    BOOK_DELTA: BookDeltaPostgres(**postgres_cfg),
                    L2_BOOK: BookPostgres(**postgres_cfg),
                    TRADES: TradePostgres(**postgres_cfg),
                },
            )
        )
        logging.info(f"{exchange} feed added.")
    logging.info("Starting crawling.")
    feed_handler.run()


def main():
    args = parse_arguments()
    symbols = list(map(str, args.symbols.strip('[]').split(',')))
    exchanges = list(map(str, args.exchanges.strip('[]').split(',')))
    crawl_book_and_trade_data(symbols, exchanges)


if __name__ == "__main__":
    logging.basicConfig(
        format="%(asctime)s %(levelname)-8s %(message)s", level=logging.INFO, datefmt="%Y-%m-%d %H:%M:%S"
    )
    main()
