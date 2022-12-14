import unittest
from stocklab.agent.data import Data
import inspect

class TestData(unittest.TestCase):
    
    def setUp(self):
        self.data = Data()
        
    def test_get_corp_code(self):
        print(inspect.stack()[0][3])
        result = self.data.get_corp_code(name="삼성전자")
        assert result is not None
        print(result)
        
    def test_get_corp_info_by_code(self):
        print(inspect.stack()[0][3])
        result = self.data.get_corp_info(code="593")
        assert result is not None
        print(result)
        
    def test_get_stk_distribution_info(self):
        print(inspect.stack()[0][3])
        result = self.data.get_stk_distribution_info(code="593", date="20181231")
        assert result is not None
        print(result)
    
    # def test_api(self):
    #     import requests
    #     print(inspect.stack()[0][3])
    #     url = 'http://api.seibro.or.kr/openapi/service/CorpSvc/getBuyreqSkeduInfoSvc'
    #     params ={'serviceKey' : 'WHBfNB5rRra7bp6+eLY6y7S6LeV2ND0wEK1HfDundXXBh0aQaBul55hthD2aqzEbaBqlqRJT5WOxedsNP+cMiQ==', 'rgtStdDt' : '20190708', 'issucoCustno' : '30411', 'pageNo' : '1', 'numOfRows' : '10' }

    #     response = requests.get(url, params=params)
    #     print(response.content)
        
    def tearDown(self):
        pass