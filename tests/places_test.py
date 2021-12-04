import unittest
from near_places import NearPlaces

class TestUserInsert(unittest.TestCase):

	def test1_call(self):
		location = "midtown atlanta"
		loc_type = "restaurant"
		actual = NearPlaces.getNearPlace(
            location,
            loc_type,
        )
		expected = ["place1", "place2", "place3"]
		self.assertEqual(len(actual), len(expected))


	def test2_call(self):
		location = "downtown atlanta"
		loc_type = "park"
		actual = NearPlaces.getNearPlace(
            location,
            loc_type,
        )
		expected = ["place1", "place2", "place3"]
		self.assertEqual(len(actual), len(expected))


	def test3_call(self):
		location = "midtown atlanta"
		loc_type = "restaurant"
		actual = NearPlaces.getNearPlace(
            location,
            loc_type,
        )
		expected = ["place1", "place2", "place3"]
		self.assertNotEqual(actual, expected)


	def test4_call(self):
		location = "downtown atlanta"
		loc_type = "park"
		actual = NearPlaces.getNearPlace(
            location,
            loc_type,
        )
		expected = ["place1", "place2", "place3"]
		self.assertNotEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()