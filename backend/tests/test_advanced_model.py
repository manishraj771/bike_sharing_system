import unittest
from ml_models.advanced_modeling import best_rf_model, best_gb_model, best_xgb_model

class TestAdvancedModels(unittest.TestCase):

    def test_random_forest(self):
        self.assertIsNotNone(best_rf_model)
        print("RandomForest test passed.")

    def test_gradient_boosting(self):
        self.assertIsNotNone(best_gb_model)
        print("GradientBoosting test passed.")

    def test_xgboost(self):
        self.assertIsNotNone(best_xgb_model)
        print("XGBoost test passed.")

if __name__ == '__main__':
    unittest.main()
