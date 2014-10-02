import unittest
import lexical_diversity

q= '#MentionSomeoneImportantForYou'
class TestLexicalDiversity(unittest.TestCase):
	def test_title(self):
		self.assertTrue(lexical_diversity.lex(q))
		
	def lexical_diversity(self):
		self.assertEqual(lexical_diversity.lexical_diversity(['one','two','three','four', 'five']), 5)
		
	def test_average_words(self):
		self.assertEqual(lexical_diversity.average_words(['one','two','three']),1)

if __name__ == "__main__":
	unittest.main()