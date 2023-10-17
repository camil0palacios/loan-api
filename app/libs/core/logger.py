import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

class LoggerBuilder:
    
    def __init__(self, logger) -> None:
        self.logger = logger
    
    def log(self, level, text):
        if level == 'INFO':
            self.logger.info(text)
        elif level == 'ERROR':
            self.logger.error(text, exc_info=True)
        elif level == 'WARNING':
            self.logger.warning(text)
        else:
            self.logger.debug(text)

Logger = LoggerBuilder(logger)
