# Cricket Stats Analyzer 
print("-------Cricket stats analyzer-----")

total_players=5

player1=int(input(f"the runs score by the player1 : "))
player2=int(input(f"the runs score by the player2 : "))
player3=int(input(f"the runs score by the player3 : "))
player4=int(input(f"the runs score by the player4 : "))
player5=int(input(f"the runs score by the player5 : "))

total_runs = (player1 + player2 + player3 + player4 + player5)
average_runs = (total_runs/total_players)


print("-------cricket statics-----")
print(f"total runs scored by all the players = {total_runs}" )
print(f"total average runs scored by all the players = {average_runs}" )