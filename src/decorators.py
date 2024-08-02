from functools import wraps
from typing import Any, Callable


def log(filename: Any) -> Callable:
    """The log decorator automatically logs the start and end of a
    function execution and the results or errors that occur"""

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                log_message = f"{func.__name__} called with args: {args}, kwargs:{kwargs}. Result: {result}"
                if filename:
                    with open(filename, "a") as f:
                        f.write(log_message + "\n")
                else:
                    print(log_message)
            except Exception as e:
                error_message = f"{func.__name__} error: {e}. Inputs:{args}, {kwargs}"
                if filename:
                    with open(filename, "a") as f:
                        f.write(error_message + "\n")
                else:
                    print(error_message)

                return result

        return wrapper

    return decorator


@log(filename="../tests/mylog.txt")
def my_function(x: int, y: int) -> int:
    return x + y


my_function(1, 2)
