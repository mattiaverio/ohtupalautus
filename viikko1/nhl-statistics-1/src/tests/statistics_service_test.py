import unittest
from enum import Enum
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_etsi_pelaaja_nimella(self):
        player = self.stats.search("Kurri")
        self.assertEqual(player.name, "Kurri")

    def test_etsi_pelaaja_nimella_ei_ole(self):
        player = self.stats.search("kissa")
        self.assertIsNone(player)

    def test_team_palauttaa_pelaajat(self):
        team_players = self.stats.team("EDM")
        self.assertEqual(len(team_players), 3)

    def test_team_palauttaa_nolla_jos_ei_pelaajia(self):
        team_players = self.stats.team("kissajoukkue")
        self.assertEqual(len(team_players), 0)

    def test_top_palauttaa_top_pisteet(self):
        top_players = self.stats.top(2)
        self.assertEqual(len(top_players), 3)
        self.assertEqual(top_players[0].name, "Gretzky")

    def test_top_palauttaa_top_maalit(self):
        top_players = self.stats.top(2, SortBy.GOALS)
        self.assertEqual(len(top_players), 3)
        self.assertEqual(top_players[0].name, "Lemieux")

    def test_top_palauttaa_top_avustukset(self):
        top_players = self.stats.top(2, SortBy.ASSISTS)
        self.assertEqual(len(top_players), 3)
        self.assertEqual(top_players[0].name, "Gretzky")

    def test_sort_by_virheellinen_enum(self):
        class FakeSortBy(Enum):
            UNDEFINED = 99
        self.stats.top(2, FakeSortBy.UNDEFINED)
