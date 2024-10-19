import polars as pl
import logging

class DataValidator:
    def __init__(self, logger: logging.Logger):
        self._logger = logger

    def validate(self, df: pl.DataFrame):
        """Perform column-wise validation on the DataFrame."""
        self._logger.info("Validating data columns...")

        # Check if 'price' contains any null or non-positive values and type
        if df["price"].is_null().sum() > 0:
            raise ValueError("The 'price' column contains null values.")
        if (df["price"] <= 0).sum() > 0:
            raise ValueError("The 'price' column contains non-positive values.")
        if not df["price"].dtype == pl.Float64:
            raise TypeError("The 'price' column should contain float values.")

        # Check if 'quantity' contains any null or non-positive values and type
        if df["quantity"].is_null().sum() > 0:
            raise ValueError("The 'quantity' column contains null values.")
        if (df["quantity"] <= 0).sum() > 0:
            raise ValueError("The 'quantity' column contains non-positive values.")
        if not df["quantity"].dtype == pl.Int64:
            raise TypeError("The 'quantity' column should contain integer values.")

        # Check if 'product_name' contains any null or empty values and type
        if df["product_name"].is_null().sum() > 0 or (df["product_name"] == "").sum() > 0:
            raise ValueError("The 'product_name' column contains null or empty values.")
        if not df["product_name"].dtype == pl.Utf8:
            raise TypeError("The 'product_name' column should contain string values.")

        self._logger.info("Data validation successful.")