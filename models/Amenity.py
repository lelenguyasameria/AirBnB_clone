import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    def test_amenity_initialization(self):
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)

    def test_amenity_name(self):
        amenity = Amenity(name="Pool")
        self.assertEqual(amenity.name, "Pool")

if __name__ == "__main__":
    unittest.main()

