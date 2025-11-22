import logging

class LoggerWebSocket():

    def __init__(self, logger_name: str, logfile: str="add_web_logs.txt", logging_level: str = "info"):
        
        self.logger = logging.getLogger(logger_name)
        self._get_logging_level(logging_level.upper())
        if self.log_level is None:
            raise TypeError("Logging level %s does not exit", logging_level) 
        self.logger.setLevel(self.log_level)
        handler = logging.FileHandler(logfile, mode='a')        
        handler.setFormatter(logging.Formatter("[%(asctime)s] %(levelname)s: %(message)s"))
        self.logger.addHandler(handler)

    def get_logger(self):
        return self.logger

    def _get_logging_level(self, level):

        match level:
            case "INFO":
                self.log_level = logging.INFO

            case "DEBUG":
                self.log_level = logging.DEBUG

            case "WARNING":
                self.log_level = logging.WARNING

            case "ERROR":
                self.log_level = logging.ERROR

            case "CRITICAL":
                self.log_level = logging.CRITICAL
            
            case _:
                self.log_level = None
