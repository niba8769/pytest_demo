import configparser
import os

config = configparser.RawConfigParser()
config.read(os.path.abspath(os.curdir) + "\\config\\config.ini")


class readconfig:

    @staticmethod
    def getappUrl():
        return config.get('commonInfo', 'url')

    @staticmethod
    def getUsername():
        return config.get("commonInfo", "username")
    @staticmethod
    def getPassword():
        return config.get("commonInfo", "password")