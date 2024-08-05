create database portfolio_manager;

use portfolio_manager;

create table holdings(asset_id int primary key, ticker varchar(10), asset_type varchar(20),qty float, avg_price float);

create table transactions(txn_id int primary key, ticker varchar(10),txn_type varchar(5),qty float, price_rate float, txn_date datetime);

create table watchlist(ticker varchar(10) primary key);