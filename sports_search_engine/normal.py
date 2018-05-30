
import records
import psycopg2

db = records.Database("postgres://localhost/clemson_stats_db")

db.query("DROP TABLE clemson_stats_db");

db.query("CREATE TABLE clemson_stats_db (rk NUMERIC(2), player VARCHAR(30), rush_att NUMERIC(3), rush_yds NUMERIC(3), rush_avg DECIMAL, rush_td NUMERIC(2))");

"""rk = [1, 2, 3, 4, 5]
player = ["Kelly Bryant", "Travis Etienne", "Tavien Feaster", "Adam Choice", "CJ Fuller"]
rush_att = [192, 107, 107, 67, 58]
rush_yds = [665, 766, 669, 326, 217]
rush_avg = [3.5, 7.2, 6.3, 4.9, 3.7]
rush_td = [11, 13, 7, 6, 3]"""

db.query("INSERT INTO clemson_stats_db VALUES (:rk, :player, :rush_att, :rush_yds, :rush_avg, :rush_td);",
 rk = 1, player = "Kelly Bryant", rush_att = 192, rush_yds = 665, rush_avg = 3.5, rush_td = 11)

db.query("INSERT INTO clemson_stats_db VALUES (:rk, :player, :rush_att, :rush_yds, :rush_avg, :rush_td);",
 rk = 2, player = "Travis Etienne", rush_att = 107, rush_yds = 766, rush_avg = 7.2, rush_td = 13)

db.query("INSERT INTO clemson_stats_db VALUES (:rk, :player, :rush_att, :rush_yds, :rush_avg, :rush_td);",
 rk = 3, player = "Tavien Feaster", rush_att = 107, rush_yds = 669, rush_avg = 6.3, rush_td = 7)

db.query("INSERT INTO clemson_stats_db VALUES (:rk, :player, :rush_att, :rush_yds, :rush_avg, :rush_td);",
 rk = 4, player = "Adam Choice", rush_att = 67, rush_yds = 326, rush_avg = 4.9, rush_td = 6)

db.query("INSERT INTO clemson_stats_db VALUES (:rk, :player, :rush_att, :rush_yds, :rush_avg, :rush_td);",
 rk = 5, player = "CJ Fuller", rush_att = 158, rush_yds = 217, rush_avg = 3.7, rush_td = 3)
