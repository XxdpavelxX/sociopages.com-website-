import unittest
import cik


class Testcik(unittest.TestCase):
	def test_getLatestFiling(self):
		self.assertEqual(cik.getLatestFiling('0001166559',filingType="13F-HR"), 'http://www.sec.gov/Archives/edgar/data/1166559/000110465914061098/0001104659-14-061098-index.htm')
	def test_getFilingTextFile(self):
		self.assertEqual(cik.getFilingTextFile('http://www.sec.gov/Archives/edgar/data/1166559/000110465914061098/0001104659-14-061098-index.htm'),'http://www.sec.gov/Archives/edgar/data/1166559/000110465914061098/0001104659-14-061098.txt')
	def test_getHoldings(self):
		self.assertTrue(cik.getHoldings('http://www.sec.gov/Archives/edgar/data/1166559/000110465914061098/0001104659-14-061098.txt'))	

if __name__ == "__main__":
	unittest.main()