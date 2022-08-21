import sqlite3

con = sqlite3.connect("database/database.sqlite")

cur = con.cursor()

#! Tabell struktur
cur.execute("drop table if exists games;")
cur.execute("drop table if exists users;")
cur.execute("PRAGMA foreign_keys = on;")
cur.execute("""create table users(
    id integer primary key autoincrement not null,
    username text not null,
    email text not null,
    firstName text not null,
    lastName text not null,
    balance float default 0.0,
    password text not null);
""")
cur.execute("""create table games(
    id integer primary key autoincrement not null,
    playerCards text not null, 
    dealerCards text not null,
    bet float not null,
    outcome text default null);
""")


#! Standard användare
cur.execute("""insert into users(username, email, firstName, lastName, password)
    values('Airbag65', 'normananton03@gmail.com', 'Anton', 'Norman', 'db63c7e38ee64bdd02601002fb27eff5')""")

#! Bekräfta databasmutationer
con.commit()
cur.close()