import unittest
from near_places import NearPlaces

class TestUserInsert(unittest.TestCase):

	def test1_call(self):
		"""
		Test Size of outcome for API call and return. 1
		"""
		location = "midtown atlanta"
		loc_type = "restaurant"
		actual = NearPlaces.getNearPlace(
            location,
            loc_type,
        )
		expected = ["place1", "place2", "place3"]
		self.assertEqual(len(actual), len(expected))


	def test2_call(self):
		"""
		Test Size of outcome for API call and return. 2
		"""
		location = "downtown atlanta"
		loc_type = "park"
		actual = NearPlaces.getNearPlace(
            location,
            loc_type,
        )
		expected = ["place1", "place2", "place3"]
		self.assertEqual(len(actual), len(expected))


	def test3_call(self):
		"""
		Test To insure that 
		"""
		location = "midtown atlanta"
		loc_type = "restaurant"
		actual = NearPlaces.getNearPlace(
            location,
            loc_type,
        )
		expected = ["place1", "place2", "place3"]
		self.assertNotEqual(actual, expected)


	def test4_call(self):
		"""
		Check for exact match when using API call.
		"""
		location = "downtown atlanta"
		loc_type = "park"
		actual = NearPlaces.getNearPlace(
            location,
            loc_type,
        )
		expected = [{'name': 'Walton Spring Park', 'photo_reference': 'http://static.panoramio.com/photos/large/62246010.jpg'}, {'name': 'International Peace Fountain', 'photo_reference': 'http://www.soulofamerica.com/soagalleries/atl/genattr/Atl-Woodruff_Intl_Peace_Fount.jpg'}, {'name': 'John Calhoun Park', 'photo_reference': 'https://66.media.tumblr.com/tumblr_m22qt4PW9Y1qc63pwo2_500.jpg'}]
		self.assertNotEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()

