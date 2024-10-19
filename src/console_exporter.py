import logging

from src.metrics_calculator import Metrics


class ConsoleExporter:
    def __init__(self, logger: logging.Logger):
        """
        Initializes the ConsoleExporter with a logger.

        :param logger: Logger instance for logging.
        """
        self._logger = logger

    def export(self, metrics: Metrics):
        """
        Exports the calculated metrics to the console.

        :param metrics: A Metrics named tuple containing the calculated metrics.
        """
        try:
            self._logger.info("Exporting metrics to console...")

            # Print each metric to the console from the named tuple
            print(f"Total Spend: {metrics.total_spend}")
            print(f"Average Purchase: {metrics.avg_purchase}")
            print(f"Max Purchase: {metrics.max_purchase}")
            print(f"Median Purchase: {metrics.median_purchase}")
            print(f"Unique Products: {metrics.unique_products}")

            self._logger.info("Metrics successfully exported to console.")

        except Exception as e:
            self._logger.error(f"An error occurred while exporting metrics: {e}")
            raise
