''' This file is for Python Unit Test Project Problem 2'''
import csv
import matplotlib.pyplot as plt
import constants as const


def stack_plot(calculated_data: dict, transformed_data: list, x_lable: str, y_lable: str,
               title: str):
    ''' pass calculated data '''
    # get all teams
    teams = set()
    for values in calculated_data.values():
        for keys in values.keys():
            teams.add(keys)
    teams = list(teams)
    all_seasons = sorted(calculated_data.keys())

    # Creating plot
    fig = plt.figure()
    stack_current_height = [0]*len(teams)
    for season_matches in transformed_data:
        plt.bar(teams, season_matches, bottom=stack_current_height)
        stack_current_height = [sum(x) for x in zip(
                                season_matches, stack_current_height)]

    fig.autofmt_xdate() # gives rotation to the x axis titles
    plt.title(title)
    plt.legend(all_seasons)
    plt.xlabel(x_lable)
    plt.ylabel(y_lable)
    plt.tight_layout()
    # show plot
    plt.show()

def transform(stacked_chart_data: dict):
    """Pass dict variable having keys as seasons
    and pass values that are sub dictionaries with teams and total matches played
    e.g. {2008: {RCB: 10, MI: 9, ...}, 2017: {RCB: 10, MI: 9, ...}, ...}
    """
    # get all teams
    teams = set()
    for values in stacked_chart_data.values():
        for keys in values.keys():
            teams.add(keys)
    teams = list(teams)
    # get season 1 team wise total matches played
    all_seasons = sorted(stacked_chart_data.keys())
    seasonwise_matches_played_by_all_teams = []
    i = 0
    for season in all_seasons:
        seasonwise_matches_played_by_all_teams.append([])
        for team in teams:
            seasonwise_matches_played_by_all_teams[i].append(
                stacked_chart_data[season].get(team, 0))
        i += 1
    return seasonwise_matches_played_by_all_teams


def calculate(csv_file_matches: str):
    '''function to get data to plot graphs'''
    with open(csv_file_matches, encoding="utf-8") as inputfile:
        season_victory_details = {}
        matches_reader = csv.DictReader(inputfile)

        for match in matches_reader:
            season_year = int(match['season'])
            winner_team = match['winner']

            season_victory_details[season_year] = (
                season_victory_details.get(season_year, {})
            )
            season_victory_details[season_year][winner_team] = (
                season_victory_details[season_year].get(winner_team, 0) + 1
            )
    return season_victory_details


def execute():
    ''' get required data from csv in dict and then call plot function'''

    season_victory_details = calculate(const.CSV_FILE_MATCHES)
    transformed_data = transform(season_victory_details)
    stack_plot(season_victory_details, transformed_data, const.TEAM,
                       const.MATCHES_WON, const.MATCHES_WON_BY_TEAM_BY_YEAR
                       )


execute()  # driver function
