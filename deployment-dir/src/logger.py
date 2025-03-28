import logging
from typing import Optional

def get_console_logger(name: Optional[str] = 'tutorial') -> logging.Logger:
    '''
    Ensures that you have a properly configured logger with a console handler that outputs debug-level and higher messages. 
    It formats log messages to include timestamps, logger names, log levels, and the messages themselves. 
    By checking if handlers are already present, it avoids adding multiple handlers to the same logger, which would result in duplicate log messages.
    The function returns a logging.Logger object.
    '''
    
    # Create logger if it doesn't exist
    logger = logging.getLogger(name)
    if not logger.handlers:
        logger.setLevel(logging.DEBUG)

        # Create console handler with formatting
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        console_handler.setFormatter(formatter)

        # Add console handler to the logger
        logger.addHandler(console_handler)

    return logger