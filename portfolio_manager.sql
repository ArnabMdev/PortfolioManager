create database portfolio_manager;

use portfolio_manager;

create table users(user_id int primary key,user_name varchar(30),password varchar(20));

create table holdings(asset_id int primary key, user_id int, ticker varchar(10), asset_type varchar(20),qty float, avg_price float, foreign key(user_id) references users(user_id));

create table transactions(txn_id int primary key, ticker varchar(10),txn_type varchar(5),qty float, price_rate float, txn_date datetime);

create table watchlist(ticker varchar(10) primary key);