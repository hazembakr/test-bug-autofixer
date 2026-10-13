import unittest
from user_service import process_user

class TestUserService(unittest.TestCase):
    def test_process_none_user(self):
        result = process_user(None)
        self.assertIsNone(result)

    def test_process_normal_user(self):
        result = process_user({"name": "Alice"})
        self.assertEqual(result, "ALICE")

if __name__ == "__main__":
    unittest.main()
