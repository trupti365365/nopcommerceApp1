import logging

class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename=".\\Logs\\automation.log",
                            format='%(asctime)s:(levelname)s:%(message)s',
                            datefmt='%m/%d/%y %I:%M:%S %p')
        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
"""utility file we created which will do the logger configuration to generate the log file for our test cases
this is one time job
when ever we call loggen() method it will return logger object
by using the logger object we will generate logs """