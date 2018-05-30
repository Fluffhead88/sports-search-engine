import records

db = records.Database("postgres://localhost/clemson_stats_db")



choice = True
while choice:
    print("""
    Clemson Rushing Statistics for 2017 Football Season

    1. Search by Player
    2. Search by Rank
    3. Input New Player Stats
    4. Exit
    """)
    choice = input("Choose a number > ")
    if choice == "1":
      player_input = input("Player? ")
      rows = db.query("SELECT * FROM clemson_stats_db WHERE player = :data ;", data = player_input)
      for row in rows:
          print(rows)
    elif choice == "2":
      player_input = input("Rank? ")
      rows = db.query("SELECT * FROM clemson_stats_db WHERE rk = :data ;", data = player_input)
      for row in rows:
          print(rows)
    elif choice == "3":
        new_rank = input("Rank? > ")
        new_player = input("Player? > ")
        new_rush_att = input("Rushing Attempts? > ")
        new_rush_yds = input("Rushing Yards? > ")
        new_rush_avg = input("Rushing Average? > ")
        new_rush_tds = input("Rushing TD's? > ")
        rows = db.query("INSERT INTO clemson_stats_db VALUES (:rk, :player, :rush_att, :rush_yds, :rush_avg, :rush_tds);",
                rk = new_rank,
                player = new_player,
                rush_att = new_rush_att,
                rush_yds = new_rush_yds,
                rush_avg = new_rush_avg,
                rush_tds = new_rush_tds
                )
        for row in rows:
            print(rows)
    elif choice == "4":
        print("\n   GO TIGERS!")
        choice = False
