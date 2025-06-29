import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

class TestSearchAPI(unittest.TestCase):

    def test_rate_limiting(self):
        for _ in range(5):
            response = client.get("/employees/search", params={"organization_id": 1})
            # Expect 422 here because filters are missing, but rate limit shouldn't trigger yet
            self.assertIn(response.status_code, [200, 422])
        response = client.get("/employees/search", params={"organization_id": 1})
        self.assertEqual(response.status_code, 429)

# if __name__ == "__main__":
#     unittest.main()
