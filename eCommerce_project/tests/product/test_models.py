import pytest

pytestmark = pytest.mark.django_db


class TestCategoryModels:
    def test_str_method(self, category_factory):
        # Arrange
        # Act
        x = category_factory(name='test_cat')
        # Assert
        assert x.__str__() == 'test_cat'


class TestBrandModels:
    def test_str_method(self, brand_factory):
        # Arrange
        # Act
        x = brand_factory(name='test_brand')
        # Assert
        assert x.__str__() == 'test_brand'


class TestProductModels:
    def test_str_method(self, product_factory):
        # Arrange
        # Act
        x = product_factory(name='test_product')
        # Assert
        assert x.__str__() == 'test_product'

