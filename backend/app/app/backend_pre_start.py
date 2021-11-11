import logging

from tenacity import after_log, before_log, retry, stop_after_attempt, wait_fixed

from sqlalchemy.orm import Session
from app.models.db_models import Bible_Book, Bible_Chapter, Bible_Verse

from app.db.session import SessionLocal

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

max_tries = 60 * 5  # 5 minutes
wait_seconds = 1


@retry(
    stop=stop_after_attempt(max_tries),
    wait=wait_fixed(wait_seconds),
    before=before_log(logger, logging.INFO),
    after=after_log(logger, logging.WARN),
)
def init() -> None:
    try:
        db = SessionLocal()
        # Try to create session to check if DB is awake
        db.execute("SELECT 1")
    except Exception as e:
        logger.error(e)
        raise e


def create_books(db: SessionLocal()) -> Bible_Book:
    try:
        books = [
            Bible_Book(title="Genesis", slug="GEN"),
            Bible_Book(title="Exodus", slug="EXO"),
            Bible_Book(title="Leviticus", slug="LEV"),
            Bible_Book(title="Numbers", slug="NUM"),
            Bible_Book(title="Deuteronomy", slug="DEU"),
            Bible_Book(title="Joshua", slug="JOS"),
            Bible_Book(title="Judges", slug="JDG"),
            Bible_Book(title="Ruth", slug="RUT"),
            Bible_Book(title="1Samuel", slug="1SA"),
            Bible_Book(title="2Samuel", slug="2SA"),
            Bible_Book(title="1Kings", slug="1KI"),
            Bible_Book(title="2Kings", slug="2KI"),
            Bible_Book(title="1Chronicles", slug="1CH"),
            Bible_Book(title="2Chronicles", slug="2CH"),
            Bible_Book(title="Ezra", slug="EZR"),
            Bible_Book(title="Nehemiah", slug="NEH"),
            Bible_Book(title="Esther", slug="EST"),
            Bible_Book(title="Job", slug="JOB"),
            Bible_Book(title="Psalms", slug="PSA"),
            Bible_Book(title="Proverbs", slug="PRO"),
            Bible_Book(title="Ecclesiastes", slug="ECC"),
            Bible_Book(title="SongofSongs", slug="SNG"),
            Bible_Book(title="Isaiah", slug="ISA"),
            Bible_Book(title="Jeremiah", slug="JER"),
            Bible_Book(title="Lamentations", slug="LAM"),
            Bible_Book(title="Ezekiel", slug="EZK"),
            Bible_Book(title="Daniel", slug="DAN"),
            Bible_Book(title="Hosea", slug="HOS"),
            Bible_Book(title="Joel", slug="JOL"),
            Bible_Book(title="Amos", slug="AMO"),
            Bible_Book(title="Obadiah", slug="OBA"),
            Bible_Book(title="Jonah", slug="JON"),
            Bible_Book(title="Micah", slug="MIC"),
            Bible_Book(title="Nahum", slug="NAM"),
            Bible_Book(title="Habakkuk", slug="HAB"),
            Bible_Book(title="Zephaniah", slug="ZEP"),
            Bible_Book(title="Haggai", slug="HAG"),
            Bible_Book(title="Zechariah", slug="ZEC"),
            Bible_Book(title="Malachi", slug="MAL"),
            Bible_Book(title="Matthew", slug="MAT"),
            Bible_Book(title="Mark", slug="MRK"),
            Bible_Book(title="Luke", slug="LUK"),
            Bible_Book(title="John", slug="JHN"),
            Bible_Book(title="Acts", slug="ACT"),
            Bible_Book(title="Romans", slug="ROM"),
            Bible_Book(title="1Corinthians", slug="1CO"),
            Bible_Book(title="2Corinthians", slug="2CO"),
            Bible_Book(title="Galatians", slug="GAL"),
            Bible_Book(title="Ephesians", slug="EPH"),
            Bible_Book(title="Philippians", slug="PHP"),
            Bible_Book(title="Colossians", slug="COL"),
            Bible_Book(title="1Thessalonians", slug="1TH"),
            Bible_Book(title="2Thessalonians", slug="2TH"),
            Bible_Book(title="1Timothy", slug="1TI"),
            Bible_Book(title="2Timothy", slug="2TI"),
            Bible_Book(title="Titus", slug="TIT"),
            Bible_Book(title="Philemon", slug="PHM"),
            Bible_Book(title="Hebrews", slug="HEB"),
            Bible_Book(title="James", slug="JAS"),
            Bible_Book(title="1Peter", slug="1PE"),
            Bible_Book(title="2Peter", slug="2PE"),
            Bible_Book(title="1John", slug="1JN"),
            Bible_Book(title="2John", slug="2JN"),
            Bible_Book(title="3John", slug="3JN"),
            Bible_Book(title="Jude", slug="JUD"),
            Bible_Book(title="Revelation", slug="REV")
        ]

        db.bulk_save_objects(books)
        db.commit()

        logging.info("Creating books of the bible")

    except:
        logging.error('NOT WORKING')


def main() -> None:
    logger.info("Initializing service")
    init()
    create_books(db=SessionLocal())
    logger.info("Service finished initializing")


if __name__ == "__main__":
    main()
