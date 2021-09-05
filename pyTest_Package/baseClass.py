import inspect
import logging

class baseClass:
    def getLoggerObj(self):
        testcaseName = inspect.stack()[1][3]      # will get the correct testcase(method) name
        logger = logging.getLogger(testcaseName)  # will add testcase name to the logs

        fileHandler = logging.FileHandler("logfile.log")  # helps in passing file location to "logger" object
        logFormat = logging.Formatter("%(asctime)s: %(levelname)s: %(name)s: %(levelname)s: %(message)s")  # format of logs
        fileHandler.setFormatter(logFormat)

        logger.addHandler(fileHandler)  # filehandler object which will take log file location

        logger.setLevel(logging.DEBUG)
        return logger

