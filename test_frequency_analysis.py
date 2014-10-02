import frequency_analysis
import unittest

q= '#MentionSomeoneImportantForYou'
class TestLexicalDiversity(unittest.TestCase):
	def test_freq(self):
		self.assertTrue(frequency_analysis.freq(q))

if __name__ == "__main__":
	unittest.main()