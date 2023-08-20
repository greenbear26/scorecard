import scorecard
import team

max_innings = int(input("How many innings? "))

away_team = team.Team()
home_team = team.Team()
scorecard = scorecard.Scorecard(home_team, away_team)

while scorecard.inning <= max_innings:
    print(scorecard.record_pitch())

if home_team.runs > away_team.runs:
    print("The home team wins!")
elif away_team.runs > home_team.runs:
    print("The away team wins!")
else:
    print("It's a tie!")
