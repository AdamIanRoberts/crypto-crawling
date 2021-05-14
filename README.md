# crypto-crawling

Crawls cryptocurrency order book and trade data from multiple possible exchange data feeds. Using the cryptofeed library, data is normalised and written to a postgres database. A full list of available exchanges can be found https://github.com/bmoscon/cryptofeed.

## Prerequesits

- Docker
- A running postgres database (instructions on creating one using docker can be found https://hub.docker.com/_/postgres)

## Setup instructions

- git clone git@github.com:AdamIanRoberts/ftx-orderbook-crawler.git
- Create a .env file containing the following (filling in each <> with the relevant information):

    ```
    POSTGRES_HOST=localhost
    POSTGRES_PORT=<local-pg-port>
    POSTGRES_DB=<database-name>
    POSTGRES_USER=<user>
    POSTGRES_PASSWORD=<password>
    ```
    
- Create 'book' and 'trades' tables in the database. Sample SQL code to create tables for demo in `postgres_tables.sql`
    
## Running the crawlers

- Navigate to the root of the project `/path/to/project/crypto-crawling`

- Ensure the docker container running the postgres database is running:

``` docker run -d -p <local-pg-port>:<docker-pg-port> --name docker-pg -e POSTGRES_PASSWORD=pg-password postgres ```

- Build the crypto-crawling docker image (I chose to name it crypto_crawler):

``` docker build --network=host -t crypto_crawler . ```

- Run a container for the symbols [XXX-XXX] and exchanges [YYYY] of interest, mapped from port <local-crawler-port> to <docker-crawler-port>:

``` docker run -d -p <local-crawler-port>:<docker-crawler-port> --network=host --name xxxxxx_yyyy_crawler crypto_crawler --symbols [XXX-XXX] --exchanges [YYYY] ```

- Check the logs.

``` docker logs xxxxxx_yyyy_crawler ```

## Stopping the crawlers

``` docker stop xxxxxx_yyyy_crawler ```
