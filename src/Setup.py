import configparser
import os
import sys


class Setup:

    def get_path():
        if getattr(sys, 'frozen', False):
            return sys._MEIPASS
        return os.path.abspath(".")

    def get_setup(section:str|None = None):
        config = configparser.ConfigParser()
        file_path = os.path.join(Setup.get_path(), "setup.ini")
        config.read(file_path)

        if section is None:
            return config
        else:
            return config[section]