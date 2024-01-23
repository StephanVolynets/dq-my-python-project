import functools
import sys
from loguru import logger
from notifiers.logging import NotificationHandler
from dotenv import load_dotenv
import os
import time

load_dotenv()
# handler_id = logger.add(sys.stderr, level="WARNING")
# logger.remove(handler_id)  # For the default handler, it's actually '0'.

logger.info("Logging 'WARNING' or higher messages only")

logger.remove()
logger.add(sys.stderr, level="DEBUG")

logger.debug("Logging 'DEBUG' messages too")

new_level = logger.level("SNAKY", no=38, color="<yellow>", icon="🐍")

logger.log("SNAKY", "Here we go!")

logger.disable("my_library")
logger.info("No matter added sinks, this message is not displayed")
logger.enable("my_library")
logger.info("This message however is propagated to the sinks")

# this is for slack notification
# handler = NotificationHandler(
#     "slack",
#     defaults={"webhook_url": os.getenv("SLACK_WEBHOOK_URL")},
#     level="ERROR",
# )
# logger.add(handler, level="ERROR")

logger.error(f"{__file__} | something's wrong!")


def logger_wraps(*, entry=True, exit=True, level="DEBUG"):
    def wrapper(func):
        name = func.__name__

        @functools.wraps(func)
        def wrapped(*args, **kwargs):
            logger_ = logger.opt(depth=1)
            start = time.time()
            if entry:
                logger_.log(
                    level, "Entering '{}' (args={}, kwargs={})", name, args, kwargs
                )
            result = func(*args, **kwargs)
            end = time.time()
            logger_.log(level, "Function '{}' executed in {:f} s", name, end - start)

            if exit:
                logger_.log(level, "Exiting '{}' (result={})", name, result)

            return result

        return wrapped

    return wrapper


@logger_wraps()
def test_timeit():
    time.sleep(1)


test_timeit()
