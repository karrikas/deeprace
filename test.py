import unittest
from reward import reward_function

class TestReard(unittest.TestCase):

    def test_upper(self):
        params = {
            "all_wheels_on_track": 1, 
            "distance_from_center": 0,
            "track_width": 20
        }
        r = reward_function(params)
        
        self.assertEqual(r, 100)

if __name__ == '__main__':
    unittest.main()