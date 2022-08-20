drop table if exists games;
drop table if exists users;

PRAGMA foreign_keys = on;

create table users(
    id integer primary key autoincrement not null,
    username text not null,
    firstName text not null,
    lastName text not null,
    balance float default 0.0,
    password text not null,
);


create table games(
    id integer primary key autoincrement not null,
    playerCards text not null, 
    dealerCards text not null,
    bet float not null,
    outcome text default null
);