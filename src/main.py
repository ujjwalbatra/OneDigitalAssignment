import click

from src.data_fetcher import DataFetcher
from src.console_exporter import ConsoleExporter
from src.metrics_calculator import MetricsCalculator
from src.utils.logger import Logger


@click.command()
@click.argument('filepath', type=click.Path(exists=True), default='input_file/purchases_v1.json')
def bootstrapper(filepath):
    """Command-line interface for parsing a JSON file and calculating statistics."""

    logger = Logger.get_logger()
    logger.info(f'Processing file: {filepath}')

    try:
        console_exporter = ConsoleExporter(logger)
        data_fetcher = DataFetcher(logger, filepath)
        metrics_calculator = MetricsCalculator(logger)

        data = data_fetcher.get_data()
        metrics = metrics_calculator.calculate(data)
        console_exporter.export(metrics)

        logger.info(f'File processed successfully: {filepath}')

    except Exception as e:
        logger.error(f'Error processing the file: {e}')
        raise


if __name__ == '__main__':
    bootstrapper()
