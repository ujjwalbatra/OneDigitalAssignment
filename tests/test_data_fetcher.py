import json
from unittest.mock import mock_open

import pytest
import logging
from src.data_fetcher import DataFetcher


@pytest.fixture
def logger():
    return logging.getLogger(__name__)


def test_get_data_success(monkeypatch, logger):
    # Mocking json.load to return test data
    test_data = [{"brand": "TestBrand", "items": [{"price": "100", "quantity": 1}]}]

    def mock_json_load(file):
        return test_data

    # Mocking open to simulate reading a file
    mock_open_file = mock_open(read_data='{"brand": "TestBrand", "items": [{"price": "100", "quantity": 1}]}')
    monkeypatch.setattr('builtins.open', mock_open_file)

    monkeypatch.setattr('json.load', mock_json_load)

    fetcher = DataFetcher(logger, 'dummy_path')
    result = fetcher.get_data()

    assert result == test_data


def test_get_data_file_not_found(monkeypatch, logger):
    def mock_open(file, mode='r'):
        raise FileNotFoundError

    monkeypatch.setattr('builtins.open', mock_open)

    fetcher = DataFetcher(logger, 'non_existent_file.json')

    with pytest.raises(FileNotFoundError):
        fetcher.get_data()

