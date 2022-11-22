''' This file is for Python Unit Test Project Problem 1'''
import csv
import matplotlib.pyplot as plt
import constants as const


def bar_plot(bar_plot_data: dict, xlabel: str, ylabel: str, title: str):
    """Pass dict variable having keys to plot on x-axis and pass values to plot on y-axis"""
    # initialisation
    x_axis_keys = list(bar_plot_data.keys())
    y_axis_values = list(bar_plot_data.values())
    fig = plt.figure()

    # creating the bar plot
    plt.bar(x_axis_keys, y_axis_values)
    fig.autofmt_xdate()  # gives rotation to the x axis titles
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.tight_layout()
    plt.xticks(x_axis_keys)
    # show plot
    plt.show()

def calculate(csv_file_matches: str):
    '''function to get data to plot graphs'''
    with open(csv_file_matches, encoding="utf-8") as inputfile:
        yearwise_matches_played = {}
        matches_reader = csv.DictReader(inputfile)

        for match in matches_reader:
            season_year = int(match['season'])
            yearwise_matches_played[season_year] = (
                yearwise_matches_played.get(season_year, 0)
                + 1
            )
    return yearwise_matches_played


def execute():
    ''' driver function'''
    # get required data from csv in dict and then call plot function

    yearwise_matches_played = calculate(const.CSV_FILE_MATCHES)
    bar_plot(yearwise_matches_played, const.YEAR,
             const.MATCHES_PLAYED, const.MATCHES_BY_TEAM_BY_YEAR
             )


execute()  # driver function
