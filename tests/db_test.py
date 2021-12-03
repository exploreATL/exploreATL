import unittest
from dbhandler import DBHandler

class TestUserInsert(unittest.TestCase):

    def test_insert(self):
        username = 'admin'
        password = 'password'
        near_places = []
        actual = DBHandler.insert_user(DBHandler, username, password, near_places)
        expected = 1
        self.assertEqual(actual, expected)


    def test_lookup_fail(self):
        username = 'iamnotreal'
        password = 'password'
        near_places = []
        actual = DBHandler.lookup_user(DBHandler, username, password)
        expected = 1
        self.assertEqual(actual, expected)
        

    def test_lookup_ok(self):
        username = 'admin1'
        password = 'password'
        near_places = []
        actual = DBHandler.lookup_user(DBHandler, username, password)
        expected = [('admin1', '5f4dcc3b5aa765d61d8327deb882cf99', None, None, [], None, None)]
        self.assertEqual(actual, expected)


    def test_update_fail(self):
        username = 'iamnotreal'
        password = 'password'
        near_places = ["Hyatt Regency Atlanta", "Hard Rock Cafe", "The Sun Dial Restaurant", "Bar & View", "Ray's In the City"]
        loc_type = "restaurant"
        location = "midtown atlanta"
        been = [True, False, False, False, False]
        review = "I liked a place because of a thing that involved other things around that place and things that were inside that place"
        actual = DBHandler.update_list(DBHandler, username, location, loc_type, near_places, been, review)
        expected = 1
        self.assertEqual(actual, expected)


    def test_update_ok(self):
        username = 'admin'
        password = 'password'
        near_places = ["Hyatt Regency Atlanta", "Hard Rock Cafe", "The Sun Dial Restaurant", "Bar & View", "Ray's In the City"]
        loc_type = "restaurant"
        location = "midtown atlanta"
        been = [True, False, False, False, False]
        review = "I liked a place because of a thing that involved other things around that place and things that were inside that place"
        actual = DBHandler.update_list(DBHandler, username, location, loc_type, near_places, been, review)
        expected = 0
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()