import unittest
from models.city import City

class TestCity(unittest.TestCase):
    def test_city_initialization(self):
        city = City()
        self.assertIsInstance(city, City)

    def test_city_name(self):
        city = City(name="New York")
        self.assertEqual(city.name, "New York")

if __name__ == "__main__":
    unittest.main()

