import logging


class Logger:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        self.formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')
        self.file_handler = logging.FileHandler('tkinter_project.log')
        self.file_handler.setFormatter(self.formatter)
        self.logger.addHandler(self.file_handler)

