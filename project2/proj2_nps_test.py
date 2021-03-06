from proj2_nps_edited import *
import unittest

class TestStateSearch(unittest.TestCase): # OK

    def site_is_in_state_list(self, site_name, site_type, site_list): # OK
        for s in site_list:
            if site_name == s.name and site_type == s.type:
                return True
        return False

    def get_site_from_list(self, site_name, site_list): # OK
        for s in site_list:
            if site_name == s.name:
                return s
        return None

    def setUp(self): # OK
        self.mi_site_list = get_sites_for_state('mi')
        self.az_site_list = get_sites_for_state('az')
        self.isle_royale = self.get_site_from_list('Isle Royale', self.mi_site_list)
        self.lake_mead = self.get_site_from_list('Lake Mead', self.az_site_list)

    def test_basic_search(self):
        self.assertEqual(len(self.mi_site_list), 7) # OK
        self.assertEqual(len(self.az_site_list), 24) # OK

        self.assertTrue(self.site_is_in_state_list('Isle Royale',
            'National Park', self.mi_site_list)) # OK
        self.assertFalse(self.site_is_in_state_list('Isle Royale',
            'National Park', self.az_site_list)) # OK

        self.assertTrue(self.site_is_in_state_list('Lake Mead',
            'National Recreation Area', self.az_site_list)) # OK
        self.assertFalse(self.site_is_in_state_list('Lake Mead',
            'National Recreation Area', self.mi_site_list)) # OK

    def test_addresses(self):
        self.assertEqual(self.isle_royale.address_street, '800 East Lakeshore Drive') # OK
        self.assertEqual(self.isle_royale.address_city, 'Houghton') # OK
        self.assertEqual(self.isle_royale.address_zip, '49931') # OK

        self.assertEqual(self.lake_mead.address_street, '601 Nevada Way') # OK
        self.assertEqual(self.lake_mead.address_city, 'Boulder City') # OK
        self.assertEqual(self.lake_mead.address_zip, '89005') # OK

    def test_str(self):
        self.assertEqual(str(self.lake_mead), "Lake Mead (National Recreation Area): 601 Nevada Way, Boulder City, NV 89005") # OK
        self.assertEqual(str(self.isle_royale), "Isle Royale (National Park): 800 East Lakeshore Drive, Houghton, MI 49931") # OK


class TestNearbySearch(unittest.TestCase):

    def place_is_in_places_list(self, place_name, places_list): # OK
        for p in places_list:
            print(p)
            if place_name == p.name:
                return True
        return False

    def test_nearby_search(self):
        site1 = NationalSite('National Monument',
            'Sunset Crater Volcano', 'A volcano in a crater.')
        site2 = NationalSite('National Park',
            'Yellowstone', 'There is a big geyser there.')

        nearby_places1 = get_nearby_places_for_site(site1)
        nearby_places2 = get_nearby_places_for_site(site2)

        self.assertTrue(self.place_is_in_places_list('Oleary Group Site', nearby_places1)) # OK
        self.assertTrue(self.place_is_in_places_list('West Thumb', nearby_places2)) # OK

class TestMapping(unittest.TestCase):

    # we can't test to see if the maps are correct, but we can test that
    # the functions don't return an error!
    def test_show_state_map(self):
        try:
            plot_sites_for_state('mi') # OK
            plot_sites_for_state('az') # OK
        except:
            self.fail()

    def test_show_nearby_map(self):
        site1 = NationalSite('National Monument',
            'Sunset Crater Volcano', 'A volcano in a crater.')
        site2 = NationalSite('National Park',
            'Yellowstone', 'There is a big geyser there.')
        try:
            plot_nearby_for_site(site1) # OK
            plot_nearby_for_site(site2) # OK
        except:
            self.fail()

if __name__ == '__main__':
    unittest.main()
