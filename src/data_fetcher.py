import json
import logging
from typing import Any, Dict, List


class DataFetcher:
    def __init__(self,
                 logger: logging.Logger,
                 file_path: str
                 ):
        """
        Initializes the DataFetcher with a logger and file path.

        :param logger: Logger instance for logging.
        :param file_path: Path to the JSON file.
        """
        self._logger = logger
        self._file_path = file_path

    def get_data(self) -> List[Dict[str, Any]]:
        """
        Reads data from a JSON file and returns it.

        :return: List of dictionaries containing data from the JSON file.
        """
        try:
            with open(self._file_path, 'r') as f:
                data = json.load(f)

            # Log the success of the operation
            self._logger.info(f"Successfully fetched data from file: {self._file_path}")
            return data

        except FileNotFoundError:
            self._logger.error(f"File not found: {self._file_path}")
            raise

        except json.JSONDecodeError:
            self._logger.error(f"Error decoding JSON from file: {self._file_path}")
            raise

        except Exception as e:
            self._logger.error(f"An error occurred while fetching data: {e}")
            raise