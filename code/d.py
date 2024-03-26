import logging 
from abc import ABC, abstractmethod

class Logger(ABC):
    """Abstract Logger class to decouple application logic from specific logging libraries."""
    
    @abstractmethod
    def log(self, message):
        pass

class LoggingLibraryLogger(Logger):
    """Concrete Logger implementation using a specific logging library."""
    
    def __init__(self, logging_library):
        self.logger = logging_library
        
    def log(self, message):
        self.logger.info(message)

class TestLogger(Logger):
    """Test Logger implementation for testing purposes."""
    
    def log(self, message):
        print("Test Log:", message)

class Application:
    """Application class utilizing logging."""
    
    def __init__(self, logger):
        self.logger = logger
    
    def do_something(self):
        self.logger.log("Doing something...")

import logging
logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    logger = LoggingLibraryLogger(logging_library=logging)
    app = Application(logger)
    app.do_something()
# 325_quiz6
