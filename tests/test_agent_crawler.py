
import inspect
import unittest
from stocklab.agent.crawler import Crawler


class TestCrawler(unittest.TestCase):
        def setUp(self):
            self.crawler = Crawler()

        # def test_crawler(self):
        #     print(inspect.stack()[0][3])
        #     self.crawler.get_news_section()
            
        def test_crawler(self):
            print(inspect.stack()[0][3])
            self.crawler.getSide()
