from django.test import TestCase
from .models import Match, Player 

# Create your tests here.

class ManyToManyTest(TestCase):
    def setUp(self): 
        # create three players
        self.player1 = Player.objects.create(name='Player 1', account_id=1, is_pro=True)
        self.player2 = Player.objects.create(name='Player 2', account_id=2, is_pro=True)
        self.player3 = Player.objects.create(name='Player 3', account_id=3, is_pro=True)

        # create three matches
        self.match1 = Match.objects.create(started_at='2019-01-01T00:00:00Z', average_mmr=1000)
        self.match2 = Match.objects.create(started_at='2019-01-01T00:00:00Z', average_mmr=2000)
        self.match3 = Match.objects.create(started_at='2019-01-01T00:00:00Z', average_mmr=3000)

        # add add all players to match 1
        self.match1.players.add(self.player1, self.player2, self.player3)

        # add player1 and player2 to match 2
        self.match2.players.add(self.player1, self.player2)

        # add player 1 to match 3
        self.match3.players.add(self.player1)

    def test_get_matches_by_player(self):
        # which matches did player 1 participate in? expect all three
        player_1_matches = self.player1.match_set.all()
        self.assertAlmostEqual(list(player_1_matches), [self.match1, self.match2, self.match3])

        # which matches did player 2 participate in? expect only match 1 and 2
        player_2_matches = self.player2.match_set.all()
        self.assertAlmostEqual(list(player_2_matches), [self.match1, self.match2])

        # which matches did player 3 participate in? expect only match 3
        player_3_matches = self.player3.match_set.all()
        self.assertAlmostEqual(list(player_3_matches), [self.match1])

    def test_get_players_by_match(self): 
        # which players participated in match 1? expect all three
        match_1_players = self.match1.players.all()
        self.assertAlmostEqual(list(match_1_players), [self.player1, self.player2, self.player3])

        # which players participated in match 2? expect only player 1 and 2
        match_2_players = self.match2.players.all()
        self.assertAlmostEqual(list(match_2_players), [self.player1, self.player2])

        # which players participated in match 3? expect only player 1
        match_3_players = self.match3.players.all()
        self.assertAlmostEqual(list(match_3_players), [self.player1])

    
