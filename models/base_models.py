import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    def test_base_model_initialization(self):
        base_model = BaseModel()
        self.assertIsInstance(base_model, BaseModel)

    def test_base_model_id_generation(self):
        base_model1 = BaseModel()
        base_model2 = BaseModel()
        self.assertNotEqual(base_model1.id, base_model2.id)

    def test_base_model_created_at(self):
        base_model = BaseModel()
        self.assertIsInstance(base_model.created_at, datetime)

    def test_base_model_updated_at(self):
        base_model = BaseModel()
        self.assertIsInstance(base_model.updated_at, datetime)

    def test_base_model_str_representation(self):
        base_model = BaseModel()
        str_repr = str(base_model)
        self.assertIn(base_model.__class__.__name__, str_repr)
        self.assertIn(base_model.id, str_repr)
        self.assertIn(str(base_model.__dict__), str_repr)

    def test_base_model_save(self):
        base_model = BaseModel()
        original_updated_at = base_model.updated_at
        base_model.save()
        self.assertNotEqual(original_updated_at, base_model.updated_at)

    def test_base_model_to_dict(self):
        base_model = BaseModel()
        obj_dict = base_model.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertIn("__class__", obj_dict)
        self.assertIn("created_at", obj_dict)
        self.assertIn("updated_at", obj_dict)
        self.assertEqual(obj_dict["__class__"], "BaseModel")

if __name__ == "__main__":
    unittest.main()

