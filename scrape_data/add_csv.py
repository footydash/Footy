import pandas as pd
import sqlite3
from scrape_data.mysql_connect import *
from scrape_data.clean_data import *
import csv

def add_data(directory, country, division):
    """
    :param database:
    :param file_path:
    :return:
    """
    conn = footy_connect()

    file_path = read_dir(directory)
    print("cleaning csv...")
    cleaner = remove_null_values(file_path, country, division)

    for x in file_path:
        with open(x, 'r') as file, conn:
            content = csv.DictReader(file, delimiter =',')
            print('***************************************')
            print('Working on uploading data for: ' + str(x))
            cursor = conn.cursor()

            for column in content:
                date = str(column['Date'])
                home_team = str(column["HomeTeam"])
                away_team = str(column["AwayTeam"])
                home_team_goals = column['FTHG']
                away_team_goals = column['FTAG']
                full_time_result = str(column['FTR'])
                country = str(column['country'])
                division = str(column['division'])
                try:
                    ht_home_goals = column['HTHG']
                    ht_away_goals = column['HTAG']
                    ht_result = str(column['HTR'])
                    home_team_shots = column['HS']
                    away_team_shots = column['AS']
                    home_team_shot_tar = column['HST']
                    away_team_shot_tar = column['AST']
                    home_corner = column['HC']
                    away_corner = column['AC']
                    home_foul = column['HF']
                    away_foul = column['AF']
                    home_yellow = column['HY']
                    away_yellow = column['AY']
                    home_red = column['HR']
                    away_red = column["AR"]
                except Exception as e:
                    continue

                sql_info = "INSERT INTO test (date, home_team, away_team, home_team_goals, away_team_goals," \
                           "full_time_results, ht_home_goals, ht_away_goals, ht_result, home_team_shots, away_team_shots," \
                           "home_team_shot_tar, away_team_shot_tar, home_corner, away_corner, home_foul, away_foul," \
                           "home_yellow, away_yellow, home_red, away_red, country, division) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s," \
                           "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                values = (date, home_team, away_team, home_team_goals, away_team_goals, full_time_result, ht_home_goals,
                          ht_away_goals, ht_result, home_team_shots, away_team_shots,home_team_shot_tar, away_team_shot_tar,
                          home_corner, away_corner, home_foul, away_foul, home_yellow, away_yellow, home_red, away_red, country, division)

                cursor.execute(sql_info, values)
                conn.commit()

            print('Finished uploading data for ' + str(x))
            print('***************************************')

# add = add_data('path','spain')
add_data('C:\\Users\\Sal Architetto\\Desktop\\New_footy_files\\footy_files\\England\\Championship',)