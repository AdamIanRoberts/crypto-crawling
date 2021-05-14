-- book
CREATE TABLE IF NOT EXISTS book (id serial PRIMARY KEY, timestamp TIMESTAMP, receipt_timestamp TIMESTAMP, exchange VARCHAR(32), symbol VARCHAR(32), data VARCHAR(MAX));

-- trades
CREATE TABLE IF NOT EXISTS trades (id serial PRIMARY KEY, timestamp TIMESTAMP, receipt_timestamp TIMESTAMP, exchange VARCHAR(32), symbol VARCHAR(32), side VARCHAR(8), amount NUMERIC(64, 32), price NUMERIC(64, 32), trade_id varchar(32), order_type VARCHAR(32));