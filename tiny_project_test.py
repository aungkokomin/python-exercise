# Write unit test for tiny_project.py
import unittest
import requests, json
from pathlib import Path
from tiny_project import FetchRepos

class TestFetchRepos(unittest.TestCase):
    def test_fetch_repos(self):
        fetcher = FetchRepos()
        data = fetcher.fetch_repos()
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 0)
        for repo in data:
            self.assertIn("name", repo) # Check if 'name key exists
            self.assertIn("stars", repo) # Check if 'stars' key exists
            # self.assertIn("test",repo)
            self.assertIsInstance(repo['name'],str) # Check if 'name' is a string type
            self.assertIsInstance(repo['stars'],int) # Check if 'stars' is an integer type

# Run the tests
if __name__ == "__main__":
    unittest.main()

