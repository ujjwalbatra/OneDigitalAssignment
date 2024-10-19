import logging


class Logger:
    """A class to encapsulate logger configuration and provide a logger instance."""

    @staticmethod
    def get_logger(level=logging.INFO):
        """Create and configure a logger instance."""

        # Create a logger with the provided name
        logger = logging.getLogger(__name__)
        logger.setLevel(level)

        # Check if the logger already has handlers (to avoid duplicate handlers)
        if not logger.hasHandlers():
            # Create a console handler
            ch = logging.StreamHandler()
            ch.setLevel(level)

            # Create a formatter and set it for the handler
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            ch.setFormatter(formatter)

            # Add the handler to the logger
            logger.addHandler(ch)

        return logger