class Constants():
    # Bballref URLs - Team Stats
    teamStatsBaseUrl = 'http://www.basketball-reference.com/teams/'
    teamStatsUrlSuffix = {
        'baseStats': '/',
            'perGameStats': '/stats_per_game_totals.html',
        'opponentPerGameStats': '/opp_stats_per_game_totals.html'
    }

    # Bballref URLs - Player Stats
    playerStatsBaseUrl = 'http://www.basketball-reference.com/leagues/NBA_'
    playerStatsUrlSuffix = {
        'perGameStats': '_per_game.html',
        'per36Stats': '_per_minute.html',
        'per100Stats': '_per_poss.html',
        'advancedStats': '_advanced.html'
    }

    # Wiki team URLs
    wikiTeamUrl = 'https://en.wikipedia.org/wiki/Wikipedia:WikiProject_National_Basketball_Association/National_Basketball_Association_team_abbreviations'
    teamList = [
        'BOS',
        'TOR',
        'NYK',
        'PHI',
        'NJN',
        'WAS',
        'ATL',
        'MIA',
        'CHA',
        'ORL',
        'CLE',
        'MIL',
        'IND',
        'CHI',
        'DET',
        'UTA',
        'OKC',
        'POR',
        'DEN',
        'MIN',
        'SAS',
        'HOU',
        'MEM',
        'NOH',
        'DAL',
        'GSW',
        'LAC',
        'SAC',
        'PHO',
        'LAL'
    ]