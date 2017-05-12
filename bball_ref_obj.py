# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
from constants import Constants

class bballRef():
    def getTeamAbbrevList(self):
        # # Wikipedia has a list of NBA teams' name abbreviations, we read the table into a dataframe (HTML class 'wikitable')
        # teamAbbrevDf = pd.read_html(
        #     io = Constants.wikiTeamUrl,
        #     header = 0,
        #     attrs = {'class': 'wikitable'}
        # )[0]
        #
        # # Cleanse the dataframe and extract just the abbreviation column to a list
        # return teamAbbrevDf[teamAbbrevDf.columns[0]].tolist()
        return Constants.teamList

    def getTeamStats(self):
        # Iterate through NBA teams to get their team stats
        #   1. For each team
        #       a. Get different types of stats
        #       b. concatenate stats by rows (horizontally)
        teamAggDf = None

        for team in self.getTeamAbbrevList():
            teamStatsAggDf = None

            print '\nStarting to scan {}'.format(team)
            for teamStatName, teamStatUrl in Constants.teamStatsUrlSuffix.iteritems():
                # Format URL to scan
                urlToScan = '{}{}{}'.format(
                    Constants.teamStatsBaseUrl,
                    team,
                    teamStatUrl
                )

                # Pull data from HTML table
                #   Notice here we do not make the first row the header because we need that row of data to compare
                #   and drop duplicate headers in the middle of the table
                print 'Checking {}'.format(urlToScan)
                teamStatsDf = pd.read_html(
                    io = urlToScan,
                    header = None,
                    attrs = {'class': 'stats_table'}
                )[0]

                # Fix some formatting issues (extra header rows in the middle of table) from bball ref
                teamStatsDf = teamStatsDf[teamStatsDf['Season'] != 'Season']
                teamStatsDf.reset_index(inplace = True)

                # Fix some formatting issues (extra columns) from bball ref
                if u' ' in teamStatsDf.columns:
                    teamStatsDf.drop(u' ', axis = 1, inplace = True)
                if u' .1' in teamStatsDf.columns:
                    teamStatsDf.drop(u' .1', axis = 1, inplace = True)

                # Since we are appending data from multiple tables, we append a prefix to each column table in order to
                #   preserve which columns came frmo which tables
                teamStatsDf.columns = ['{}_{}'.format(str(teamStatName).encode('utf-8'), str(col).encode('utf-8')) for col in teamStatsDf.columns]

                # Aggregate stats dataframes
                if teamStatsAggDf is None:
                    teamStatsAggDf = teamStatsDf
                else:
                    teamStatsAggDf = pd.concat([teamStatsAggDf, teamStatsDf], axis = 1)

            # Aggregate stats dataframes
            if teamAggDf is None:
                teamAggDf = teamStatsAggDf
            else:
                teamAggDf = pd.concat([teamAggDf, teamStatsAggDf], axis = 0)

            print 'Finished scanning {}'.format(team)

        teamAggDf.to_csv('C:\Temp\{}.csv'.format('test'), encoding = 'utf-8')