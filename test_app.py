import unittest
import requests


class TestAPI(unittest.TestCase):
    BASE_URL = "http://127.0.0.1:5001/analyze"

    def test_analyze_text(self):
        data = {'text': 'This is a test text. This is a test.'}
        response = requests.post(self.BASE_URL, json=data)
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertEqual(result['total_words'], 9)
        self.assertCountEqual(result['top_words'], [('this', 2), ('is', 2), ('a', 2), ('test', 2)]) 

    def test_missing_text(self):
        response = requests.post(self.BASE_URL, json={})
        self.assertEqual(response.status_code, 400)


if __name__ == '__main__':
    unittest.main()
