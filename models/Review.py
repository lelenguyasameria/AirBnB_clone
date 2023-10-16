import unittest
from models.review import Review

class TestReview(unittest.TestCase):
    def test_review_initialization(self):
        review = Review()
        self.assertIsInstance(review, Review)

    def test_review_text(self):
        review = Review(text="Great place!")
        self.assertEqual(review.text, "Great place!")

    def test_review_place_id(self):
        review = Review(place_id="12345")
        self.assertEqual(review.place_id, "12345")

if __name__ == "__main__":
    unittest.main()

