import pytest
import logging
import test_demologging_subfile

#set custom logger and it's level
logger_main = logging.getLogger(__name__)
logger_main.setLevel(logging.INFO)

#configure the handler and formatter
handler_main = logging.FileHandler(f"logs/{__name__}.log",mode='w')
formatter_main = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")

# add formatter to the handler
handler_main.setFormatter(formatter_main)
# add handler to the logger
logger_main.addHandler(handler_main)

logger_main.info(f"Testing the custom logger for module {__name__}...")



def test_division():
    """testcase: it's for division operation """
    x_vals = [2, 3, 6, 4, 10]
    y_vals = [5, 7, 12, 8, 1]
    for x_val,y_val in zip(x_vals,y_vals):
        x,y = x_val, y_val
        # call test_division
        try:
            x / y
            logger_main.info(f"x/y successful with result: {x / y}.")
            assert True
        except ZeroDivisionError as err:
            logger_main.exception("ZeroDivisionError")
            assert False
        logger_main.info(f"Call test_division with args {x} and {y}")







