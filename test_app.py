import unittest
import requests


class TestAPI(unittest.TestCase):
    BASE_URL = "http://127.0.0.1:5001/analyze"

    def test_analyze_text(self):
        data = {'text': 'a a a b b c'}
        response = requests.post(self.BASE_URL, json=data)
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertEqual(result['total_words'], 6)
        self.assertCountEqual(
            result['top_words'],
            [
                ['a', 3], ['b', 2], ['c', 1]
            ]
        )

    def test_missing_text(self):
        response = requests.post(self.BASE_URL, json={})
        self.assertEqual(response.status_code, 400)


if __name__ == '__main__':
    unittest.main()
