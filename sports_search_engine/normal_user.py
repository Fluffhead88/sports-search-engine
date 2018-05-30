import records

db = records.Database("postgres://localhost/clemson_stats_db")

player_input = input("Player? ")

rows = db.query("SELECT * FROM clemson_stats_db WHERE player = :data ;", data = player_input)

for row in rows:
    print(row.player)

new_rank = input("New Rank? ")
new_player = input("New Player? ")
new_rush_att = input("New Rushing Attempts? ")
new_rush_yds = input("New Rushing Yards? ")
new_rush_avg = input("New Rushing Average? ")

db.query("INSERT INTO clemson_stats_db VALUES (:rk, :player, :rush_att, :rush_yds, :rush_avg);",
        rk = new_rank,
        player = new_player,
        rush_att = new_rush_att,
        rush_yds = new_rush_yds,
        rush_avg = new_rush_avg
        )
