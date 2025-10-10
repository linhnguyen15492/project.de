from config import log_config

try:
    log_config.log_config()
except FileNotFoundError as e:
    print(e)
    raise
