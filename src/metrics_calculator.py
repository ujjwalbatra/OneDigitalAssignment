from typing import NamedTuple

import polars as pl


class Metrics(NamedTuple):
    total_spend: float
    max_purchase: float
    median_purchase: float
    unique_products: int

class MetricsCalculator:
    def __init__(self, logger):
        """Initialize with raw data and logger."""
        self._logger = logger

    def _prepare_dataframe(self, data):
        """Create and transform a Polars DataFrame from the nested structure."""
        df = pl.DataFrame(data)

        # Explode the 'items' column (since it's a list of dictionaries)
        df = df.explode('items')

        # Unpack the dictionary in the 'items' column into individual columns
        df = df.with_columns([
            pl.col("items").struct.field("department").alias("department"),
            pl.col("items").struct.field("product_category").alias("product_category"),
            pl.col("items").struct.field("product_name").alias("product_name"),
            pl.col("items").struct.field("price").cast(pl.Float64).alias("price"),  # Convert price to float
            pl.col("items").struct.field("quantity").alias("quantity"),
        ])

        # Calculate the total price for each item (price * quantity)
        df = df.with_columns((pl.col("price") * pl.col("quantity")).alias("total_price"))

        # Drop the original 'items' column as it's no longer needed
        df = df.drop('items')

        return df

    def calculate(self, data):
        """Calculate the metrics for the batch."""

        df = self._prepare_dataframe(data)
        total_spend = df["total_price"].sum()
        max_purchase = df["total_price"].max()
        median_purchase = df["total_price"].median()
        unique_products = df["product_name"].n_unique()

        return Metrics(
            total_spend=total_spend,
            max_purchase=max_purchase,
            median_purchase=median_purchase,
            unique_products=unique_products
        )
