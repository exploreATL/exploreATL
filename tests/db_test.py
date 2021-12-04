import unittest
from dbhandler import DBHandler

class TestUserInsert(unittest.TestCase):
    '''
    Unit Test for Server Database Handling with Server and Client Side Handoff.
    '''
    def test_insert(self):
        """
        Test for user insert failure when there is already a user registered under that name
        """
        username = 'admin'
        password = 'password'
        near_places = []
        actual = DBHandler.insert_user(DBHandler, username, password, near_places)
        expected = 1
        self.assertEqual(actual, expected)


    def test_lookup_fail(self):
        """
        Test for user look up when there is a failure to find that user.
        """
        username = 'iamnotreal'
        password = 'password'
        near_places = []
        actual = DBHandler.lookup_user(DBHandler, username, password)
        expected = 1
        self.assertEqual(actual, expected)
        

    def test_lookup_ok(self):
        """
        Test for user look up success, when user is new and has not data other than init data.
        """
        username = 'admin1'
        password = 'password'
        near_places = []
        actual = DBHandler.lookup_user(DBHandler, username, password)
        expected = [('admin1', '5f4dcc3b5aa765d61d8327deb882cf99', None, None, [], None, None)]
        self.assertEqual(actual, expected)


    def test_update_fail(self):
        """
        Tests for when a non exist user is tryed to update  that user's user data and should fail.
        """
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
        """
        Test for user data update, and has a 0 on success.
        """
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
