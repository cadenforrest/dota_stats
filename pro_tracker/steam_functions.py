import requests
import secret


BASE_STEAM_URL = "http://api.steampowered.com/"
GET_MATCH_HISTORY = "IDOTA2Match_570/GetMatchHistory/v001/"
GET_MATCH_HISTORY_BY_SEQ_NUM = "IDOTA2Match_570/GetMatchHistoryBySequenceNum/v0001/"
GET_MATCH_DETAILS = "IDOTA2Match_570/GetMatchDetails/v001/"
GET_LEAGUE_LISTING = "IDOTA2Match_570/GetLeagueListing/v0001/"
GET_LIVE_LEAGUE_GAMES = "IDOTA2Match_570/GetLiveLeagueGames/v0001/"
GET_TEAM_INFO_BY_TEAM_ID = "IDOTA2Match_570/GetTeamInfoByTeamID/v001/"
GET_PLAYER_SUMMARIES = "ISteamUser/GetPlayerSummaries/v0002/"
GET_HEROES = "IEconDOTA2_570/GetHeroes/v0001/"
GET_GAME_ITEMS = "IEconDOTA2_570/GetGameItems/v0001/"
GET_TOURNAMENT_PRIZE_POOL = "IEconDOTA2_570/GetTournamentPrizePool/v1/"
GET_TOP_LIVE_GAME = "IDOTA2Match_570/GetTopLiveGame/v1/"
BASE_ITEMS_IMAGES_URL = "http://cdn.dota2.com/apps/dota2/images/items/"
BASE_HERO_IMAGES_URL = "http://cdn.dota2.com/apps/dota2/images/heroes/"




def get_top_live_matches():
    """ Returns a dictionary of the top live matches from lord Gaben's API. """
    return requests.get(
        BASE_STEAM_URL + GET_TOP_LIVE_GAME,
        params={"partner": "partner", "key": secret.STEAM_API_KEY},
    ).json()
