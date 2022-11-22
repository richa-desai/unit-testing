''' This file is for Python Unit Test Project Problem 3'''
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


def get_match_ids_of_a_year(year: str, matches_csv: str):
    ''' function to get match ids of year 2016'''
    matches_reader = csv.reader(open(r"matches.csv", encoding="utf-8"))
    filtered_matches = list(
        filter(lambda match: year == match[1], matches_reader))

    match_ids_of_2016 = []
    for match in filtered_matches:
        match_ids_of_2016.append(match[0])
    return match_ids_of_2016


def calculate(data_source_csv: str):
    ''' function to get data to plot all graphs'''
    match_ids_of_2016 = get_match_ids_of_a_year("2016", "matches.csv")
    with open(data_source_csv, encoding="utf-8") as inputfile:
        extra_runs_in_2016 = {}
        deliveries_reader = csv.DictReader(inputfile)

        for delivery in deliveries_reader:
            extra_runs_in_this_ball = int(delivery['extra_runs'])

            if delivery['match_id'] in match_ids_of_2016:
                extra_runs_in_2016[delivery['bowling_team']] = (
                    extra_runs_in_2016.get(
                        delivery['bowling_team'], 0
                    )
                    + extra_runs_in_this_ball
                )
    return extra_runs_in_2016

def execute():
    ''' get required data from csv in dict and then call appropriate plot functions'''

    extra_runs_in_2016 = calculate(const.CSV_FILE_DELIVERY)

    bar_plot(extra_runs_in_2016, const.TEAM,
                const.TOT_EXTRA_RUNS, const.EXTRA_RUNS_2016)


execute()  # driver function
