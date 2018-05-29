
import records
import psycopg2

db = records.Database("postgres://localhost/clemson_data")


db.query(CREATE TABLE clemson_data (
rk NUMERIC(2),
player VARCHAR(30),
rush_att NUMERIC(3),
rush_yds NUMERIC(3),
rush_avg DECIMAL,
rush_td NUMERIC(2),
recv_recp NUMERIC(2),
recv_yds NUMERIC(3),
recv_avg DECIMAL,
recv_td NUMERIC(2),
scrim_plays NUMERIC(3),
scrim_yds NUMERIC(3),
scrim_avg DECIMAL,
scrim_td NUMERIC(3)
);
# drop table and create table

rk = [1, 2]

db.query("INSERT INTO clemson_data VALUES (:rk, :player, :rush_att, :rush_yds, :rush_avg,
        :rush_td, :recv_recp, :recv_yds, :recv_avg, :recv_td, :scrim_plays, :scrim_yds,
        :scrim_avg, :scrim_td);")

for rank in rk:
    db.query.append(rk)

DROP TABLE clemson_data;
