import logging


logger = logging.getLogger(__name__)

logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler('logger/app.log')

console_handler = logging.StreamHandler()

file_handler.setLevel(logging.DEBUG)
console_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)
