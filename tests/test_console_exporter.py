import logging
from src.metrics_calculator import Metrics
from src.console_exporter import ConsoleExporter
import pytest


@pytest.fixture
def logger():
    return logging.getLogger(__name__)


def test_export_metrics_success(capsys, logger):
    exporter = ConsoleExporter(logger)
    metrics = Metrics(
        total_spend=1000.0,
        avg_purchase=500.0,
        max_purchase=700.0,
        median_purchase=500.0,
        unique_products=2
    )

    exporter.export(metrics)

    captured = capsys.readouterr()

    assert "Total Spend: 1000.0" in captured.out
    assert "Average Purchase: 500.0" in captured.out
    assert "Max Purchase: 700.0" in captured.out
    assert "Median Purchase: 500.0" in captured.out
    assert "Unique Products: 2" in captured.out


def test_export_metrics_error(monkeypatch, logger):
    def mock_export_failure(metrics):
        raise Exception("Export Error")

    monkeypatch.setattr(ConsoleExporter, "export", mock_export_failure)

    exporter = ConsoleExporter(logger)

    with pytest.raises(Exception):
        exporter.export(Metrics(0, 0, 0, 0, 0))
