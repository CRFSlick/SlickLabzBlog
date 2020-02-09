import re
import datetime
import traceback


class Log(object):

    def __init__(self, filename='log', extension='txt', directory='./'):
        """
        Creates Log object

        Args:
            filename (str): name of log file [Default: log]
            extension (str): extension of log file [Default: txt]
            directory (str): location of log file relative to this file [Default: ./]
        """

        self.caller = self.__get_caller()
        self.filename = self.__validate_data(filename, 'filename', 'str')
        self.extension = self.__validate_data(extension, 'extension', 'str')
        self.directory = self.__validate_data(directory, 'directory', 'str')

    def out(self, message, level='info'):
        """
        Writes data to the log file

        Args:
            message (str): message that is to be logged
            level (str): level of particular log [Default: INFO]
        """

        message = self.__validate_data(message, 'message', 'str')
        level = self.__validate_data(level, 'level', 'str')

        level = level.upper()
        now = str(datetime.datetime.now())
        with open(f'{self.directory}{self.filename}.{self.extension}', 'a+') as log:
            log.write(f'{now} | {self.caller} | {level}: {message}')
            log.write('\n')

    def clear(self):
        """
        Clears log file, but does not delete it

        Args:
            None
        """
        open(self.directory + self.filename + '.' + self.extension, 'w+')
        return

    @staticmethod
    def __validate_data(data, name, data_type):
        if data_type == 'str':
            try:
                assert isinstance(data, str)
                return str(data)
            except (AssertionError, ValueError):
                raise ValueError(f"expected '{name}' to be of type {data_type}, but got {type(data)}!")

    @staticmethod
    def __get_caller():
        """
        Gets the file name of the caller

        Args:
            None
        """
        back_slash = '\\'
        forward_slash = '/'
        filename = traceback.format_stack()[0]
        filename = re.findall('(?:^[^_]*")(.*)"(?:[^_]*)', filename)[0]

        if back_slash in filename:
            filename = filename.split(back_slash)[len(filename.split(back_slash)) - 1]
        if forward_slash in filename:
            filename = filename.split(forward_slash)[len(filename.split(forward_slash)) - 1]
        else:
            # raise Exception('Something went wrong when getting caller off of stack!')\
            return "Unknown"

        return filename
