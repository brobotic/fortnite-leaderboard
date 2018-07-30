from app import app, db
from app.models import Stats, WinFeed, StatsFour, StatsLifetime
import requests
import json
from datetime import datetime
from pytz import timezone
import pytz
from bs4 import BeautifulSoup
from time import sleep

players = ['jamzzee', 'brobotic', 'jambijon', 'irishleadhead', 'hustleb0nez']

API_KEY = 'API key from FortniteTracker'
headers = {API_KEY}

def get_stats():
    for player in players:
        print(player)
        r = requests.get('https://api.fortnitetracker.com/v1/profile/pc/{0}'.format(player), headers=headers)
        data = json.loads(r.text)

        player_statsfour = StatsFour.query.filter_by(player=player).order_by(StatsFour.id.desc()).first()
        player_statslife = StatsLifetime.query.filter_by(player=player).order_by(StatsLifetime.id.desc()).first()

        '''
        Season 4 stats
        '''

        # Season 4 Solo
        if 'curr_p2' not in data['stats']:
            print('No games played in this bracket. Skipping')
        else:

            # Season 4 Solo Wins
            s4_s_wins = data['stats']['curr_p2']['top1']['valueInt']

            if s4_s_wins > player_statsfour.s4_solo_wins:
                print(f'Updating s4_solo_wins: New - {s4_s_wins}, Old - {player_statsfour.s4_solo_wins}')
                player_statsfour.s4_solo_wins = s4_s_wins

            # Season 4 Solo Kills
            s4_s_kills = data['stats']['curr_p2']['kills']['valueInt']

            if s4_s_kills > player_statsfour.s4_solo_kills:
                print(f'Updating s4_solo_kills: New - {s4_s_kills}, Old - {player_statsfour.s4_solo_kills}')
                player_statsfour.s4_solo_kills = s4_s_kills

            # Season 4 Solo Max Kills/Game
            s4_s_kills_max_check = get_highest_kills('p2', data)

            if s4_s_kills_max_check > player_statsfour.s4_solo_killsmax:
                print(f"Updating s4_solo_killsmax. New: {s4_s_kills_max_check}, Old {player_statsfour.s4_solo_killsmax}")
                player_statsfour.s4_solo_killsmax = s4_s_kills_max_check

            # Season 4 Solo K/D
            player_statsfour.s4_solo_kd = data['stats']['curr_p2']['kd']['valueDec']

            # Season 4 Solo Matches Played
            s4_s_matches = data['stats']['curr_p2']['matches']['valueInt']

            if s4_s_matches > player_statsfour.s4_solo_matches:
                print(f'Updating s4_solo_matches: New: {s4_s_matches}, Old - {player_statsfour.s4_solo_matches}')
                player_statsfour.s4_solo_matches = s4_s_matches

            # Season 4 Solo WinRate
            if 'winRatio' not in data['stats']['curr_p2']:
                print('No games played. Skipping.')
            else:
                player_statsfour.s4_solo_wr = data['stats']['curr_p2']['winRatio']['valueDec']

        # Season 4 Duo
        if 'curr_p10' not in data['stats']:
            print('No games played in this bracket. Skipping')
        else:

            # Season 4 Duo Wins
            s4_d_wins = data['stats']['curr_p10']['top1']['valueInt']

            if s4_d_wins > player_statsfour.s4_duo_wins:
                print(f'Updating s4_duo_wins: New - {s4_d_wins}, Old - {player_statsfour.s4_duo_wins}')
                player_statsfour.s4_duo_wins = s4_d_wins

            # Season 4 Duo Kills
            s4_d_kills = data['stats']['curr_p10']['kills']['valueInt']

            if s4_d_kills > player_statsfour.s4_duo_kills:
                print(f'Updating s4_duo_kills: New - {s4_d_kills}, Old - {player_statsfour.s4_duo_kills}')
                player_statsfour.s4_duo_kills = s4_d_kills

            # Season 4 Duo Max Kills/Game
            s4_d_kills_max_check = get_highest_kills('p10', data)

            if s4_d_kills_max_check > player_statsfour.s4_duo_killsmax:
                print(f'Updating s4_duo_killsmax: New - {s4_d_kills_max_check}, Old - {player_statsfour.s4_duo_killsmax}')
                player_statsfour.s4_duo_killsmax = s4_d_kills_max_check
    
            # Season 4 Duo K/D
            player_statsfour.s4_duo_kd = data['stats']['curr_p10']['kd']['valueDec']

            # Season 4 Duo Matches Played
            s4_d_matches = data['stats']['curr_p10']['matches']['valueInt']

            if s4_d_matches > player_statsfour.s4_duo_matches:
                print(f'Updating s4_duo_matches: New: {s4_d_matches}, Old - {player_statsfour.s4_duo_matches}')
                player_statsfour.s4_duo_matches = s4_d_matches

            # Season 4 Duo WinRate
            if 'winRatio' not in data['stats']['curr_p10']:
                print('No games played. Skipping.')
            else:
                player_statsfour.s4_duo_wr = data['stats']['curr_p10']['winRatio']['valueDec']

        # Season 4 Squad
        if 'curr_p9' not in data['stats']:
            print('No games played in this bracket. Skipping')
        else:

            # Season 4 Squad Wins
            s4_sq_wins = data['stats']['curr_p9']['top1']['valueInt']

            if s4_sq_wins > player_statsfour.s4_squad_wins:
                print(f'Updating s4_squad_wins: New - {s4_sq_wins}, Old - {player_statsfour.s4_squad_wins}')
                player_statsfour.s4_squad_wins = s4_sq_wins

            # Season 4 Squad Kills
            s4_sq_kills = data['stats']['curr_p9']['kills']['valueInt']

            if s4_sq_kills > player_statsfour.s4_squad_kills:
                print(f'Updating s4_squad_kills: New - {s4_sq_kills}, Old - {player_statsfour.s4_squad_kills}')
                player_statsfour.s4_squad_kills = s4_sq_kills

            # Season 4 Squad Max Kills/Game
            s4_sq_kills_max_check = get_highest_kills('p9', data)

            if s4_sq_kills_max_check > player_statsfour.s4_squad_killsmax:
                print(f'Updating s4_squad_killsmax: New - {s4_sq_kills_max_check}, Old - {player_statsfour.s4_squad_killsmax}')
                player_statsfour.s4_squad_killsmax =  s4_sq_kills_max_check

            # Season 4 Squad K/D
            player_statsfour.s4_squad_kd = data['stats']['curr_p9']['kd']['valueDec']

            # Season 4 Squad Matches Played
            s4_sq_matches = data['stats']['curr_p9']['matches']['valueInt']

            if s4_sq_matches > player_statsfour.s4_squad_matches:
                print(f'Updating s4_squad_matches: New: {s4_sq_matches}, Old - {player_statsfour.s4_squad_matches}')
                player_statsfour.s4_squad_matches = s4_sq_matches

            # Season 4 Squad WinRate
            if 'winRatio' not in data['stats']['curr_p9']:
                print('No games played. Skipping.')
            else:
                player_statsfour.s4_squad_wr = data['stats']['curr_p9']['winRatio']['valueDec']

        # Season 4 Total Wins / Kills Matches
        s4_wins = total_stats(s4_s_wins, s4_d_wins, s4_sq_wins)
        
        if s4_wins > player_statsfour.s4_total_wins:
            print(f'Updating s4_total_wins: New - {s4_wins}, Old - {player_statsfour.s4_total_wins}')
            player_statsfour.s4_total_wins = s4_wins

        # Season 4 Total Kills
        s4_kills = total_stats(s4_s_kills, s4_d_kills, s4_sq_kills)

        if s4_kills > player_statsfour.s4_total_kills:
            print(f'Updating s4_total_kills: New - {s4_kills}, Old - {player_statsfour.s4_total_kills}')
            player_statsfour.s4_total_kills = s4_kills

        # Season 4 Total Matches
        s4_matches = total_stats(s4_s_matches, s4_d_matches, s4_sq_matches)

        if s4_matches > player_statsfour.s4_total_matches:
            print(f'Updating s4_total_matches: New - {s4_matches}, Old - {player_statsfour.s4_total_matches}')
            player_statsfour.s4_total_matches = s4_matches

        '''
        Lifetime stats
        '''

        # Lifetime Wins
        lt_wins = int(data['lifeTimeStats'][8]['value'])

        if lt_wins > player_statslife.life_wins:
            print(f'Updating life_wins: New - {lt_wins}, Old - {player_statslife.life_wins}')
            player_statslife.life_wins = lt_wins

        # Lifetime Kills
        lt_kills = int(data['lifeTimeStats'][10]['value'])
        
        if lt_kills > player_statslife.life_kills:
            print(f'Updating life_kills: New - {lt_kills}, Old - {player_statslife.life_kills}')
            player_statslife.life_kills = lt_kills

        # Lifetime K/D
        player_statslife.life_kd = float(data['lifeTimeStats'][11]['value'])

        # Lifetime Matches Played
        lt_matches = int(data['lifeTimeStats'][7]['value'])

        if lt_matches > player_statslife.life_matches:
            print(f'Updating life_matches: New - {lt_matches}, Old - {player_statslife.life_matches}')
            player_statslife.life_matches = lt_matches

        # Lifetime WinRate
        lt_wr_raw = data['lifeTimeStats'][9]['value']
        # Casting to float is required because lifeTimeStats data only returns the value as a string
        player_statslife.life_wr = float(lt_wr_raw[:-1])

        # Lifetime Solo Wins
        lt_s_wins = data['stats']['p2']['top1']['valueInt']

        if lt_s_wins > player_statslife.life_solo_wins:
            print(f'Updating life_solo_wins: New - {lt_s_wins}, Old - {player_statslife.life_solo_wins}')
            player_statslife.life_solo_wins = lt_s_wins

        # Lifetime Solo Kills
        lt_s_kills = data['stats']['p2']['kills']['valueInt']

        if lt_s_kills > player_statslife.life_solo_kills:
            print(f'Updating life_solo_kills: New - {lt_s_kills}, Old - {player_statslife.life_solo_kills}')
            player_statslife.life_solo_kills = lt_s_kills

        # Lifetime Solo K/D
        player_statslife.life_solo_kd = data['stats']['p2']['kd']['valueDec']     

        # Lifetime Solo Matches Played
        lt_s_matches = data['stats']['p2']['matches']['valueInt']

        if lt_s_matches > player_statslife.life_solo_matches:
            print(f'Updating life_solo_matches: New - {lt_s_matches}, Old - {player_statslife.life_solo_matches}')
            player_statslife.life_solo_matches = lt_s_matches

        # Lifetime Solo WinRate
        if 'winRatio' not in data['stats']['p2']:
            print('No games played. Skipping.')
        else:
            player_statslife.life_solo_wr = data['stats']['p2']['winRatio']['valueDec']

        # Lifetime Duo Wins
        lt_d_wins = data['stats']['p10']['top1']['valueInt']

        if lt_d_wins > player_statslife.life_duo_wins:
            print(f'Updating life_duo_wins: New - {lt_d_wins}, Old - {player_statslife.life_duo_wins}')
            player_statslife.life_duo_wins = lt_d_wins

        # Lifetime Duo Kills
        lt_d_kills = data['stats']['p10']['kills']['valueInt']

        if lt_d_kills > player_statslife.life_duo_kills:
            print(f'Updating life_duo_kills: New - {lt_d_kills}, Old - {player_statslife.life_duo_kills}')
            player_statslife.life_duo_kills = lt_d_kills

        # Lifetime Duo K/D
        player_statslife.life_duo_kd = data['stats']['p10']['kd']['valueDec']     

        # Lifetime Duo Matches Played
        lt_d_matches = data['stats']['p10']['matches']['valueInt']

        if lt_d_matches > player_statslife.life_duo_matches:
            print(f'Updating life_duo_matches: New - {lt_d_matches}, Old - {player_statslife.life_duo_matches}')
            player_statslife.life_duo_matches = lt_d_matches

        # Lifetime Duo WinRate
        if 'winRatio' not in data['stats']['p10']:
            print('No games played. Skipping.')
        else:
            player_statslife.life_duo_wr = data['stats']['p10']['winRatio']['valueDec']

        # Lifetime Squad Wins
        lt_sq_wins = data['stats']['p9']['top1']['valueInt']

        if lt_sq_wins > player_statslife.life_squad_wins:
            print(f'Updating life_squad_wins: New - {lt_sq_wins}, Old - {player_statslife.life_squad_wins}')
            player_statslife.life_squad_wins = lt_sq_wins

        # Lifetime Squad Kills
        lt_sq_kills = data['stats']['p9']['kills']['valueInt']

        if lt_sq_kills > player_statslife.life_squad_kills:
            print(f'Updating life_squad_kills: New - {lt_sq_kills}, Old - {player_statslife.life_squad_kills}')
            player_statslife.life_squad_kills = lt_sq_kills

        # Lifetime Duo K/D
        player_statslife.life_squad_kd = data['stats']['p9']['kd']['valueDec']      

        # Lifetime Duo Matches Played
        lt_sq_matches = data['stats']['p9']['matches']['valueInt']

        if lt_sq_matches > player_statslife.life_squad_matches:
            print(f'Updating life_squad_matches: New - {lt_sq_matches}, Old - {player_statslife.life_squad_matches}')
            player_statslife.life_squad_matches = lt_sq_matches

        # Lifetime Duo WinRate
        if 'winRatio' not in data['stats']['p9']:
            print('No games played. Skipping.')
        else:
            player_statslife.life_squad_wr = data['stats']['p9']['winRatio']['valueDec']     

        get_wins(data)
        sleep(2)
    db.session.commit()

def total_stats(solo_stat, duo_stat, squad_stat):
    return int(solo_stat) + int(duo_stat) + int(squad_stat)

def convert_time(mTime):
    # mTime is passed in using this format: 2018-05-08T04:43:12.823

    # We remove the T from the middle of the string and turn it into a space: 2018-05-08T04:43:12.823    
    mTime = mTime.replace('T', ' ')
    
    # Trim off the milliseconds: 2018-05-08 04:43:12
    mTimeSplit = mTime.split(".")[0]

    # Turn it into a datetime object: datetime.datetime(2018, 5, 8, 4, 43, 12)
    dt_utc_naive = datetime.strptime(mTimeSplit, '%Y-%m-%d %H:%M:%S')

    # Set it to UTC format: datetime.datetime(2018, 5, 8, 4, 43, 12, tzinfo=<UTC>
    dt_utc = dt_utc_naive.replace(tzinfo=pytz.utc)

    # Convert to PST: datetime.datetime(2018, 5, 7, 21, 43, 12, tzinfo=<DstTzInfo 'US/Pacific' PDT-1 day, 17:00:00 DST>)
    dt_pst = dt_utc.astimezone(timezone('US/Pacific'))

    # Turn it back into a plain old string so it can be added to the database: 2018-05-07 21:43:12
    m_Time = datetime.strftime(dt_pst, '%Y-%m-%d %H:%M:%S')
    return m_Time

def get_mode(modeType):
    if modeType == "p10":
        return "duo"
    elif modeType == "p9":
        return "squad"
    elif modeType == "p2":
        return "solo"
    else:
        print('nothing')

def get_highest_kills(mode, winData):
    kill_list = []
    for w in winData['recentMatches']:
        if mode not in w['playlist']:
            continue
        else:
            kills = w['kills']
            kill_list.append(kills)
    
    if kill_list:
        kills_highest = max(kill_list)
        return kills_highest
    else:
        return 0

def get_wins(winData):
    player = winData['epicUserHandle']
    for d in winData['recentMatches']:
        if d['top1'] == 1:
            kills = d['kills']
            modeName = get_mode(d['playlist'])
            matchTime = convert_time(d['dateCollected'])
            log = "{} {} won a {} match with {} kills".format(matchTime, player, modeName, kills)
            exists = WinFeed.query.filter_by(log=log).first()
            if not exists:
                print(f'New win: {log}')
                db.session.add(WinFeed(log=log))

get_stats()