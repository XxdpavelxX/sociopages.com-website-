import unittest
import fb_popularity

class TestFbPopularity(unittest.TestCase):
    def test_popularity(self):
        self.assertTrue(fb_popularity.popularity('Megaman', 'DragonBallZ'))
    def test_compare(self):
        self.assertEqual(fb_popularity.compare('Megaman', 'DragonBallZ'), "DragonBallZ is more popular than Megaman.")
		self.assertEqual(fb_popularity.compare('Digimon', 'Megaman'), "Digimon is more popular than Megaman.")
		self.assertEqual(fb_popularity.compare('Megaman', 'Megaman'), "Both pages are equally popular")
if __name__ == "__main__":
    unittest.main()