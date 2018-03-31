# You have volunteered to be the Coordinator for your town’s youth soccer league.
#  As part of your job you need to divide the 18 children who have signed up for the league into three even teams
#  - Dragons, Sharks and Raptors. In years past, the teams have been unevenly matched, so this year you are doing your
#  best to fix that. For each child, you will have the following information: Name, height (in inches), whether or not
#  they have played soccer before, and their guardians’ names. You'll take a list of these children, divide them into
#  teams and output a text file listing the three teams and the players on them. There are three main tasks you'll
#  need to complete to get this done
# In your Python program, read the data from the supplied CSV file. Store that data in an appropriate data type
#  so that it can be used in the next task.
# Create logic that can iterate through all 18 players and assign them to teams such that each team has the same
#  number of players. The number of experienced players on each team should also be the same.
# Finally, the program should output a text file named -- teams.txt -- that contains the league roster
#  listing the team name, and each player on the team including the player's information: name,
#  whether they've played soccer before and their guardians' names.

import csv

experience_players = []
novice_players = []
teams = [
    {
        "name": "Sharks",
        "list_of_players": []
    },
    {
        "name": "Dragons",
        "list_of_players": []
    },
    {
        "name": "Raptors",
        "list_of_players": []
    },
]


def extract_lists(dict_reader_obj):
    for player in dict_reader_obj:
        if player['Soccer Experience'].upper() == 'YES':
            experience_players.append(player)
        else:
            novice_players.append(player)


def distribute_experience():
    amount_experience = len(experience_players) // len(teams)
    teams[0]['list_of_players'] = experience_players[:amount_experience]
    teams[1]['list_of_players'] = experience_players[amount_experience:(amount_experience * 2)]
    teams[2]['list_of_players'] = experience_players[(amount_experience * 2):]


def distribute_novice():
    amount_novice = len(novice_players) // len(teams)
    teams[0]['list_of_players'].extend(novice_players[:amount_novice])
    teams[1]['list_of_players'].extend(novice_players[amount_novice:(amount_novice * 2)])
    teams[2]['list_of_players'].extend(novice_players[(amount_novice * 2):])


def export_list():
    file = open("teams.txt", "w")
    for team in teams:
        file.write("\n\n")
        file.write((team["name"] + ":\n\n"))
        for player in team["list_of_players"]:
            file.write(", ".join([player["Name"], player["Soccer Experience"], player["Guardian Name(s)"], "\n"]))
    file.close()


if __name__ == "__main__":
    with open('soccer_players.csv', newline='') as csvfile:
        dict_reader_obj = csv.DictReader(csvfile)
        extract_lists(dict_reader_obj)
        distribute_experience()
        distribute_novice()
        export_list()
