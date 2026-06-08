import logging

## logging setting
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler("app1.log"),    # logs to file
        logging.StreamHandler()     # logs to console we can't log to console with filename and filemode
    ]
)

logger = logging.getLogger("ArithmeticApp")

def add(a,b):
    logger.debug(f"Adding {a} + {b}: {a + b}")
    return a + b

def sub(a,b):
    logger.debug(f"Subtracting {a} - {b}: {a - b}")
    return a - b

def mul(a,b):
    logger.debug(f"Multiplying {a} * {b}: {a * b}")
    return a * b

def div(a,b):
    try:
        result = a / b
        logger.debug(f"Dividing {a} / {b}: {a / b}")
        return result
    except ZeroDivisionError:
        logger.error("Division by zero error")
        return None
    
add(12, 46)
sub(32, 12)
mul(52, 62)
div(25, 0)