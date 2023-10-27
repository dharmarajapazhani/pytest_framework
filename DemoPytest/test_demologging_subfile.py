import pytest
import logging

#create logger
logger2 = logging.getLogger(__name__)
logger2.setLevel(logging.INFO)

# configure the handler and formatter for logger2
handler2 = logging.FileHandler(f"logs/{__name__}.log", mode='w')
formatter2 = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")

# add formatter to the handler
handler2.setFormatter(formatter2)
# add handler to the logger
logger2.addHandler(handler2)

logger2.info(f"Testing the custom logger for module {__name__}...")

def test_demologging_subfile():
    """testcase, sample subfile demo , hence mark it as True bye default"""
    assert True
