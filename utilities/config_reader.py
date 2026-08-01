import configparser

config = configparser.RawConfigParser()
config.read("config.ini")

class ReadConfig:

    @staticmethod
    def get_base_url():
        return config.get("common info", "baseURL")

    @staticmethod
    def get_browser():
        return config.get("common info", "browser")