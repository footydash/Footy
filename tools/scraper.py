import pandas as pd
import datetime
import time
import requests
import numpy as np
from bs4 import BeautifulSoup
import lxml
import html5lib

class Scraper:

    paths = {'live': 'https://www.livescore.cz/live-soccer.php',
             'today': 'https://www.livescore.cz/index.php',
             'yesterday': 'https://www.livescore.cz/yesterday.php',
             'tomorrow': 'https://www.livescore.cz/tomorrow.php'}

    def __init__(self, path):
        self.path = path


    def live_scores(path):
        """

        :return:
        """
        try:
            r = requests.get(path)
            soup = BeautifulSoup(r.content, "html.parser")
            df = pd.read_html(r.content, attrs={'class': 'tab main-live'})[0]
            return df
        except ValueError as e:
            return "No live games on right now"


def change_data(df, live=False):
        if live is not False:
            return df.rename(columns={0: 'Game Start', 1: 'Current Time', 2: 'Home Team',
                                      3: 'Score', 4: 'Away Team'})
        else:
            return df.rename(columns={0: 'Game Start', 1: 'Division', 2: 'Home Team' ,3: 'Score',
                                      4: 'Away Team'})

# class ScraperTest:
#
#     live = 'https://www.livescore.cz/live-soccer.php',
#     today = 'https://www.livescore.cz/index.php',
#     yesterday = 'https://www.livescore.cz/yesterday.php',
#     tomorrow = 'https://www.livescore.cz/tomorrow.php'
#
#     def __init__(self, live, today, yesterday, tomorrow):
#         self.live = live.live
#         self.today = today.today
#         self.yesterday = yesterday.yesterday
#         self.tomorrow = tomorrow.tomorrow
#
#     def live_scores(self, path):
#         """
#
#         :return:
#         """
#         try:
#             if
#             r = requests.get(path)
#             soup = BeautifulSoup(r.content, "html.parser")
#             df = pd.read_html(r.content, attrs={'class': 'tab main-live'})[0]
#             return df
#         except ValueError as e:
#             return "No live games on right now"

    # def change_data(df):
    #     if Scraper.paths == Scraper.paths['live']:
    #         return df.rename(columns={0: 'Game Start', 1: 'Current Time', 2: 'Home Team',
    #                                   3: 'Score', 4: 'Away Team'})
    #     else:
    #         return df.rename(columns={0: 'Game Start', 1: 'Home Team', 3: 'Score',
    #                                   4: 'Away Team'})

