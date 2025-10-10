import logging
import logging.config
import os.path


def log_config():
    config = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "standard": {"format": "%(asctime)s [%(levelname)s] %(name)s: %(message)s"},
        },
        "handlers": {
            "console": {
                "class": "logging.FileHandler",
                "level": "DEBUG",
                "formatter": "standard",
                "filename": os.path.join("logs", "etl_pipeline.log"),
            },
        },
        "loggers": {
            "": {"handlers": ["console"], "level": "DEBUG", "propagate": False}
        },
    }
    logging.config.dictConfig(config)


if __name__ == "__main__":
    log_config()
