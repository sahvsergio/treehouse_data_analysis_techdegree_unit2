import time
import sys
from statistics import mean


def greet(balanced_teams, teams):

    app_title = 'BASKETBALL TEAM STATS TOOL'
    menu_str = '---MENU---'
    instructions = ['Here are your choices',
                    '1) Display Team Stats',
                    '2) Quit'
                    ]
    team_instructions = [' 1) Panthers', '2) Bandits', '3) Warriors']

    good_bye = 'Bye, Thank you for visiting the '
    print(app_title.center(100))
    print(menu_str.center(100))

    print()
    print()
    for instruction in instructions:
        print(instruction)
    while True:
        print()
        print()
        selections = input('Enter an option \u25B6'.center(50))
        if selections == '1':
            for team_instruction in team_instructions:
                print(team_instruction)

            team = input('Enter the team name \u25B6'.center(50))

            if team.title() in teams:
                print(f'Team: {team.title()} stats'.center(127))
                deco = '-'*20
                print(deco.center(127))
                print(f'total players:{len(balanced_teams[team.title()])}')
                list_of_heights = []
                experienced = []
                inexperienced = []
                for player in balanced_teams[team.title()]:
                    list_of_heights.append(player['Height'])
                    if player['Experience'] is True:
                        experienced.append(player)

                    else:
                        inexperienced.append(player)

                print(f'Experienced: {len(experienced)}')
                print(f'Inexperienced: {len(inexperienced)}')
                average_height = mean(list_of_heights)
                print(f'Average Height:{average_height:.2f}')
                print()
                print()
                print('players on teams:'.center(127))
                list_of_players = []
                list_of_guardians = []

                for player in balanced_teams[team.title()]:
                    list_of_players.append(f'{player['First Name']} {player['Last Name']}')
                    guards = player['Guardians']
                    for guard in guards:
                        list_of_guardians.append(guard)
                        list_of_guardians.append(guard)
                player_on_teams = ','.join(list_of_players)
                guards_on_team = ','.join(list_of_guardians)

                print('These are the players in this team :')
                print(player_on_teams)
                print()
                print()
                print('These are the guardians for all players in this teams:')
                print()
                print(str(guards_on_team))

            else:
                print('Please enter a valid  team option'.center(70))

        elif selections == '2':
            print()
            print()
            print(f'Thank you for visiting {app_title}.Hope to see you again, soon')
            sys.exit()
        else:
            print('Please enter a valid option'.center(70))
