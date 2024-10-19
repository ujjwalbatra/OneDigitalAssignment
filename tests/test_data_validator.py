import logging
import polars as pl
import pytest
from src.data_validator import DataValidator


@pytest.fixture
def logger():
    return logging.getLogger(__name__)


def test_validate_success(logger):
    data = {
        "price": [100.0, 200.0],
        "quantity": [1, 2],
        "product_name": ["Item1", "Item2"]
    }
    df = pl.DataFrame(data)

    validator = DataValidator(logger)
    validator.validate(df)


def test_validate_null_price(logger):
    data = {
        "price": [None, 200.0],
        "quantity": [1, 2],
        "product_name": ["Item1", "Item2"]
    }
    df = pl.DataFrame(data)

    validator = DataValidator(logger)

    with pytest.raises(ValueError):
        validator.validate(df)


def test_validate_non_positive_price(logger):
    data = {
        "price": [-100.0, 200.0],
        "quantity": [1, 2],
        "product_name": ["Item1", "Item2"]
    }
    df = pl.DataFrame(data)

    validator = DataValidator(logger)

    with pytest.raises(ValueError):
        validator.validate(df)


def test_validate_wrong_dtype_price(logger):
    data = {
        "price": ["wrong_type", "200.0"],
        "quantity": [1, 2],
        "product_name": ["Item1", "Item2"]
    }
    df = pl.DataFrame(data)

    validator = DataValidator(logger)

    with pytest.raises(TypeError):
        validator.validate(df)