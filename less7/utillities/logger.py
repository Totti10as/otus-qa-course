import inspect
import logging


def customLogger(logLevel=logging.DEBUG):


    # Gets the name of the class / method from where this method is called
    loggerName = inspect.stack()[1][3]
    #logging.config.fileConfig('logging.conf')
    logger = logging.getLogger(loggerName)
    # By default, log all messages
    logger.setLevel(logging.DEBUG)

    fileHandler = logging.FileHandler('C:/Users/Totti10/PycharmProjects/otus-qa-course/less7/logs/automation.log', mode='a')
    fileHandler.setLevel(logLevel)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)

    return logger
