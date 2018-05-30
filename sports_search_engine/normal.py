
import records
import psycopg2

db = records.Database("postgres://localhost/clemson_stats_db")


db.query("CREATE TABLE clemson_stats_db (rk NUMERIC(2), player VARCHAR(30), rush_att NUMERIC(3), rush_yds NUMERIC(3), rush_avg DECIMAL, rush_td NUMERIC(2))");

rk = [1, 2, 3, 4, 5]
player = ["Kelly Bryant", "Travis Etienne", "Tavien Feaster", "Adam Choice", "CJ Fuller"]
rush_att = [192, 107, 107,67, 58]
rush_yds = [665, 766, 669, 326, 217]
rush_avg = [3.5, 7.2, 6.3, 4.9, 3.7]
rush_td = [11, 13, 7, 6, 3]

db.query("INSERT INTO clemson_stats_db VALUES (:rk, :player, :rush_att, :rush_yds, :rush_avg, :rush_td,);")

for rank in rk:
    db.query.append(rk)
for player in player:
    db.query.append(player)
for rush_att in rush_att:
    db.query.append(rush_att)
for rush_yds in rush_yds:
    db.query.append(rush_yds)
for rush_avg in rush_avg:
    db.query.append(rush_avg)
for rush_td in rush_td:
    db.query.append(rush_td)

"DROP TABLE clemson_stats_db";
