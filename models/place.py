import unittest
from models.place import Place

class TestPlace(unittest.TestCase):
    def test_place_initialization(self):
        place = Place()
        self.assertIsInstance(place, Place)

    def test_place_name(self):
        place = Place(name="Cozy Cottage")
        self.assertEqual(place.name, "Cozy Cottage")

    def test_place_max_guest(self):
        place = Place(max_guest=4)
        self.assertEqual(place.max_guest, 4)

if __name__ == "__main__":
    unittest.main()

