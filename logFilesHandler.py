import logging
import os

logging.basicConfig(filename='tmp.log',
                    format='%(levelname)s %(asctime)s :: %(message)s',
                    level=logging.DEBUG)
# format is a formatter string, level shows what level of logs it will record
# in this case it is everything!
# Levels are as follows from most to least critical
#   CRITICAL
#   ERROR
#   WARNING
#   INFO
#   DEBUG

do = True
yes = True
do_the_work = lambda: None

def outerLog(mainFunction):
    def innerLog(*args, **kwargs):
        print('hello')
        logging.info(mainFunction.__name__+' Function Startd')
        try:
            mainFunction(*args, **kwargs)
            logging.info(mainFunction.__name__ + ' No Error Found.')
        except Exception as e:
            logging.error(mainFunction.__name__ + ' Function Got Error : '+str(e))
        logging.info(mainFunction.__name__ + ' Function Ended')
        print('hi')
    return innerLog
    # return outerLog



#======================================================================
from logFile import outerLog, logging
logger = logging.getLogger()
logger.disabled = True
@outerLog
def hello():
    print('this is just a test')
    logging.info('hello i am inside.')


hello()

logger.disabled = False
@outerLog
def hello2():
    print('this is just a test')
    logging.info('hello i am inside.')
hello2()
