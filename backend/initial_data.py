import logging

from backend.db.init_db import init_db
from backend.db.session import SessionLocal
from autopopulate_books import get_verses


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def init() -> None:
    db = SessionLocal()
    init_db(db)


def main() -> None:
    logger.info("Creating initial data")
    init()
    get_verses()
    logger.info("Initial data created")


if __name__ == "__main__":
    main()
