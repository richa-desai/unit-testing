''' This file is for Python Data Project Problem 1'''
import csv
import unittest
import matplotlib.pyplot as plt
import constants as const
from functions import bar_plot


def calculate():
    '''function to get data to plot graphs'''
    with open(const.CSV_FILE_MATCHES, encoding="utf-8") as inputfile:
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

    yearwise_matches_played = calculate()

    bar_plot(yearwise_matches_played, const.YEAR,
             const.MATCHES_PLAYED, const.MATCHES_BY_TEAM_BY_YEAR
             )
    # show plot
    plt.show()


execute()  # driver function
