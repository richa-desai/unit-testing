''' this file is for IPL prj (Python Data Project) Problem 1, 2, 7 and 8'''
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


def transform(bowlerwise_runs: dict, top_n: int):
    ''' function to get top n bowlers'''
    ball_count = "Ball count"
    bowler_run = "Bowler runs"
    for bowler in bowlerwise_runs:
        bowlerwise_runs[bowler] = (
            bowlerwise_runs[bowler][bowler_run] /
            bowlerwise_runs[bowler][ball_count]
        )

    runs_bowler = list(bowlerwise_runs.values())
    runs_bowler.sort()
    bottom_n_average = runs_bowler[:top_n]

    top_bowler_economy = {}
    for value in bottom_n_average:
        for bowler_name, bowler_average in bowlerwise_runs.items(): 
            if bowler_average == value:
                top_bowler_economy[bowler_name] = bowler_average

    return top_bowler_economy

def get_match_ids_of_a_year(year: str, matches_csv: str):
    ''' function to get match ids of year 2016'''

    with open(matches_csv, encoding="utf-8") as inputfile:
        matches_reader = csv.DictReader(inputfile)
        match_ids_of_2016 = []

        for match in matches_reader:
            if match['season'] == year:
                match_ids_of_2016.append(match['id'])

    return match_ids_of_2016


def calculate(deliveries_csv: str):
    ''' Calculate top bowlers of 2015 '''
    match_ids_of_2015 = get_match_ids_of_a_year("2015", "mock_matches.csv")

    # get required data from csv in dict and then call appropriate plot functions
    with open(deliveries_csv, encoding="utf-8") as inputfile:
        bowlerwise_runs_2015 = {}
        deliveries_reader = csv.DictReader(inputfile)
        ball_count = "Ball count"
        bowler_run = "Bowler runs"

        for delivery in deliveries_reader:
            delivery_bowler = delivery['bowler']

            if delivery['match_id'] in match_ids_of_2015:
                bowlerwise_runs_2015[delivery_bowler] = (
                    bowlerwise_runs_2015.get(
                        delivery_bowler, {}
                    )
                )
                bowlerwise_runs_2015[delivery_bowler][bowler_run] = (
                    bowlerwise_runs_2015[delivery_bowler].get(
                        bowler_run, 0
                    )
                    + int(delivery['total_runs'])
                )
                bowlerwise_runs_2015[delivery_bowler][ball_count] = (
                    bowlerwise_runs_2015[delivery_bowler].get(
                        ball_count, 0
                    )
                    + 1
                )

    return bowlerwise_runs_2015


def execute():
    ''' function to get data to plot all graphs'''

    bowlerwise_runs_2015 = calculate(const.CSV_FILE_DELIVERY)
    top_bowlers_of_2015 = transform(bowlerwise_runs_2015, 10) # get top 10
    bar_plot(top_bowlers_of_2015, const.PLAYERS,
                const.ECONOMY, const.TOP_BOWLER_2015)


execute()  # driver function
