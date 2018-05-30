import records

db = records.Database("postgres://localhost/clemson_stats_db")



choice = True
while choice:
    print("""
    Clemson Rushing Statistics for 2017 Football Season
    1.Search by Player
    2.Search by Rank
    3.Input New Player Stats
    4.Exit/Quit
    """)
    choice = input("Choose a number > ")
    if choice == "1":
      player_input = input("Player? ")
      rows = db.query("SELECT * FROM clemson_stats_db WHERE player = :data ;", data = player_input)
      for row in rows:
          print(row.player)
    elif choice == "2":
        pass
    elif choice == "3":
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
    elif choice == "4":
        print("\n Goodbye")
        choice = False
