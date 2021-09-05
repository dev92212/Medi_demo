import logging

def test_loggingDemo():
    logger = logging.getLogger(__name__)                #will add testcase name to the logs

    fileHandler = logging.FileHandler("logfile.log")    #helps in passing file location to "logger" object
    logFormat = logging.Formatter("%(asctime)s: %(levelname)s: %(name)s: %(levelname)s: %(message)s")       #formatin which to print
    fileHandler.setFormatter(logFormat)

    logger.addHandler(fileHandler)                      #filehandler object which will take log file location

    logger.setLevel(logging.DEBUG)
    logger.debug("Level_1: Debug statement")
    logger.info("Level_2: Information statement")
    logger.warning("Level_3: Warning statement")
    logger.error("Level_4: Error statement")
    logger.critical("Level_5: Critical statement")
