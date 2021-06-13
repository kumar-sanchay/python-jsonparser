import json
import unittest
from json_parser import JSONParser


class TestJSONParser(unittest.TestCase):

    def setUp(self):
        file = open('test.json')
        self.data_json = json.load(file)
    
    def test_json_parser(self):

        class TestJson(JSONParser):
            id = '_id'
            index = 'index'
            guid = 'guid'
            tags = 'tags/$1'
        
        obj = TestJson(self.data_json, many=True)
        expected_data = [{'id': '60c5ae8031f79979388eccb1', 'index': 0, 'guid': 'a5f24d6b-6889-45e4-8892-89f95df2ba88', 'tags': 'quis'}, {'id': '60c5ae80d9691296373b3ef1', 'index': 1, 'guid': '900f5e2d-8793-46d3-9325-a011caf32238', 'tags': 'cillum'}, {'id': '60c5ae80271f32f09e5ea415', 'index': 2, 'guid': '09c1ec02-b569-4914-9397-b67f644b9a1d', 'tags': 'exercitation'}, {'id': '60c5ae80f406c1eb31950ee9', 'index': 3, 'guid': '92d62973-54ad-483b-aff8-79051152a450', 'tags': 'magna'}, {'id': '60c5ae80285ddbb99530b0f6', 'index': 4, 'guid': '004231c8-4be5-4113-a81e-57fc00d6c026', 'tags': 'esse'}, {'id': '60c5ae80fb7f300484df0355', 'index': 5, 'guid': 'f4f326cb-f887-43f2-8a40-55ce410ceb53', 'tags': 'voluptate'}, {'id': '60c5ae80bb391a013cad503e', 'index': 6, 'guid': '2da5e3ad-9034-4054-ba02-88a646ec793c', 'tags': 'eiusmod'}]

        self.assertEqual(obj.validate(), expected_data)


if __name__=='__name__':
    unittest.main()