FROM python:3.8

ADD crypto_crawling/ ./crypto_crawling/
ADD requirements.txt ./
ADD .env ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENTRYPOINT ["python", "-m", "crypto_crawling.crawling.crawl_book_and_trade_data"]
CMD ["--symbols", "[BTC-USDT]", "--exchanges", "[BINANCE]"]