import polars as pl
import pytest

from src.metrics_calculator import MetricsCalculator, Metrics


@pytest.fixture
def logger():
    import logging
    return logging.getLogger('test_logger')


def test_prepare_dataframe(logger):
    """Test if the dataframe is prepared correctly."""
    data = [
        {
            "items": [
                {"department": "Tools", "price": 100, "quantity": 1, "product_name": "Item1",
                 "product_category": "Hardware"},
                {"department": "Electronics", "price": 200, "quantity": 2, "product_name": "Item2",
                 "product_category": "Devices"}
            ]
        }
    ]

    calculator = MetricsCalculator(logger)
    df = calculator.prepare_dataframe(data)

    # Check the shape of the DataFrame (2 rows, 6 columns)
    assert df.shape == (2, 6)
    # Check that required columns exist
    assert set(df.columns) == {'department', 'product_category', 'product_name', 'price', 'quantity', 'total_price'}
    # Check column data types
    assert df['price'].dtype == pl.Float64
    assert df['quantity'].dtype == pl.Int64
    assert df['total_price'].dtype == pl.Float64
    # Check content of the 'total_price' column
    assert df['total_price'].to_list() == [100.0, 400.0]


def test_calculate_metrics(logger):
    """Test if the metrics are calculated correctly."""
    data = [
        {
            "items": [
                {"department": "Tools", "price": 100, "quantity": 1, "product_name": "Item1",
                 "product_category": "Hardware"},
                {"department": "Electronics", "price": 200, "quantity": 2, "product_name": "Item2",
                 "product_category": "Devices"}
            ]
        }
    ]

    calculator = MetricsCalculator(logger)
    df = calculator.prepare_dataframe(data)

    metrics = calculator.calculate(df)

    # Check calculated metrics
    assert metrics.total_spend == 500.0  # Total of all purchases (100 + 400)
    assert metrics.avg_purchase == 250.0  # Average of total purchases (100 + 400) / 2
    assert metrics.max_purchase == 400.0  # Maximum single purchase value (200 * 2)
    assert metrics.median_purchase == 250.0  # Median of [100, 400]
    assert metrics.unique_products == 2  # Two unique products


def test_empty_dataframe(logger):
    """Test that metrics calculator handles empty dataframes correctly."""
    calculator = MetricsCalculator(logger)

    # Create an empty dataframe with the expected schema
    df = pl.DataFrame({
        'department': [],
        'product_category': [],
        'product_name': [],
        'price': pl.Float64,
        'quantity': pl.Int64,
        'total_price': pl.Float64
    })

    metrics = calculator.calculate(df)

    # Check that metrics are 0 or NaN as appropriate
    assert metrics.total_spend == 0.0
    assert metrics.avg_purchase == 0.0
    assert metrics.max_purchase == 0.0
    assert metrics.median_purchase == 0.0
    assert metrics.unique_products == 0