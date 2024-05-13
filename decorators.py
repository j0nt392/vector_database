import time
import logging

# Set up logging configuration at the start of your program
logging.basicConfig(
    filename='errors.log',
    level=logging.WARNING,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logging.captureWarnings(True)

# Decorator to measure the time taken by a function to execute
def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} executed in: {end - start:.4f} seconds")
        return result
    return wrapper

# Log errors and warnings that occur in a function
def log_errors(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logging.error(f"Error in {func.__name__}: {e}", exc_info=True)
            print(f"Error in {func.__name__}: {e}")
            return None  # Optional: depends on whether you want to return a value on error
    return wrapper
