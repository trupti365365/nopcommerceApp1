import configparser

config=configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")
class ReadConfig:
    @staticmethod
    def getApplicationURL(): #i can call this method any where without creating an object
        url=config.get('common info','baseURL')
        return url
    """@staticmethod
    def getUseremail():
        username=config.get('common info','useremail')
        return username
    @staticmethod
    def getPassword():
        password=config.get('common info','password')
        return password
    this is how we created utilities file to read the data from ini file
    in test case we have to call this methods """