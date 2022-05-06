import logging

FORMATTER = logging.Formatter("%(astime)s-%(name)s - %(levelname)s -%(message)s")
LOG_FILE = "my_app.log"

def get_console_handler():
	consol_handler = logging.StreamHandler()
	consol_handler.setFormatter(FORMATTER)
	return console_handler

def get_file_handler(log_file=LOG_FILE):
	file_handler = logging.FileHandler(log_file)
	file_handler.setFormatter(FORMATTER)
	return file_handler

def get_logger(logger_name, enable_console=False, level =logging.INFO):
	logger = logging.getLogger(logger_name)
	logger.setLevel(level)
	if enable_console:
		logger.addHandler(get_console_handler())
	logger.addHandler(get_file_handler(LOG_FILE))
	return logger