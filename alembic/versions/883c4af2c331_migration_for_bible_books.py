"""migration for bible books


Revision ID: 883c4af2c331
Revises: bc83f3380051
Create Date: 2021-11-16 23:42:08.710472

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import Table, MetaData


# revision identifiers, used by Alembic.
revision = '883c4af2c331'
down_revision = 'bc83f3380051'
branch_labels = None
depends_on = None


def upgrade():

    meta = MetaData(bind=op.get_bind())

    # pass in tuple with tables we want to reflect, otherwise whole database will get reflected
    meta.reflect(only=('bible_book',))

    # define table representation
    bible_book_tbl = Table('bible_book', meta)

    # insert records
    op.bulk_insert(
        bible_book_tbl,
        [
            {"title": "Genesis", "slug": "GEN", "chapter_count": 50},
            {"title": "Exodus", "slug": "EXO", "chapter_count": 40},
            {"title": "Leviticus", "slug": "LEV", "chapter_count": 27},
            {"title": "Numbers", "slug": "NUM", "chapter_count": 36},
            {"title": "Deuteronomy", "slug": "DEU", "chapter_count": 34},
            {"title": "Joshua", "slug": "JOS", "chapter_count": 24},
            {"title": "Judges", "slug": "JDG", "chapter_count": 21},
            {"title": "Ruth", "slug": "RUT", "chapter_count": 4},
            {"title": "1 Samuel", "slug": "1SA", "chapter_count": 31},
            {"title": "2 Samuel", "slug": "2SA", "chapter_count": 24},
            {"title": "1 Kings", "slug": "1KI", "chapter_count": 22},
            {"title": "2 Kings", "slug": "2KI", "chapter_count": 25},
            {"title": "1 Chronicles", "slug": "1CH", "chapter_count": 29},
            {"title": "2 Chronicles", "slug": "2CH", "chapter_count": 36},
            {"title": "Ezra", "slug": "EZR", "chapter_count": 10},
            {"title": "Nehemiah", "slug": "NEH", "chapter_count": 13},
            {"title": "Esther", "slug": "EST", "chapter_count": 13},
            {"title": "Job", "slug": "JOB", "chapter_count": 42},
            {"title": "Psalms", "slug": "PSA", "chapter_count": 150},
            {"title": "Proverbs", "slug": "PRO", "chapter_count": 31},
            {"title": "Ecclesiastes", "slug": "ECC", "chapter_count": 12},
            {"title": "Song of Solomon", "slug": "SNG", "chapter_count": 8},
            {"title": "Isaiah", "slug": "ISA", "chapter_count": 66},
            {"title": "Jeremiah", "slug": "JER", "chapter_count": 52},
            {"title": "Lamentations", "slug": "LAM", "chapter_count": 5},
            {"title": "Ezekiel", "slug": "EZK", "chapter_count": 48},
            {"title": "Daniel", "slug": "DAN", "chapter_count": 12},
            {"title": "Hosea", "slug": "HOS", "chapter_count": 14},
            {"title": "Joel", "slug": "JOL", "chapter_count": 3},
            {"title": "Amos", "slug": "AMO", "chapter_count": 9},
            {"title": "Obadiah", "slug": "OBA", "chapter_count": 1},
            {"title": "Jonah", "slug": "JON", "chapter_count": 4},
            {"title": "Micah", "slug": "MIC", "chapter_count": 4},
            {"title": "Nahum", "slug": "NAM", "chapter_count": 3},
            {"title": "Habakkuk", "slug": "HAB", "chapter_count": 3},
            {"title": "Zephaniah", "slug": "ZEP", "chapter_count": 3},
            {"title": "Haggai", "slug": "HAG", "chapter_count": 2},
            {"title": "Zechariah", "slug": "ZEC", "chapter_count": 14},
            {"title": "Malachi", "slug": "MAL", "chapter_count": 4},
            {"title": "Matthew", "slug": "MAT", "chapter_count": 28},
            {"title": "Mark", "slug": "MRK", "chapter_count": 16},
            {"title": "Luke", "slug": "LUK", "chapter_count": 24},
            {"title": "John", "slug": "JHN", "chapter_count": 21},
            {"title": "Acts", "slug": "ACT", "chapter_count": 28},
            {"title": "Romans", "slug": "ROM", "chapter_count": 16},
            {"title": "1 Corinthians", "slug": "1CO", "chapter_count": 16},
            {"title": "2 Corinthians", "slug": "2CO", "chapter_count": 13},
            {"title": "Galatians", "slug": "GAL", "chapter_count": 6},
            {"title": "Ephesians", "slug": "EPH", "chapter_count": 6},
            {"title": "Philippians", "slug": "PHP", "chapter_count": 4},
            {"title": "Colossians", "slug": "COL", "chapter_count": 4},
            {"title": "1 Thessalonians", "slug": "1TH", "chapter_count": 5},
            {"title": "2 Thessalonians", "slug": "2TH", "chapter_count": 3},
            {"title": "1 Timothy", "slug": "1TI", "chapter_count": 6},
            {"title": "2 Timothy", "slug": "2TI", "chapter_count": 4},
            {"title": "Titus", "slug": "TIT", "chapter_count": 3},
            {"title": "Philemon", "slug": "PHM", "chapter_count": 1},
            {"title": "Hebrews", "slug": "HEB", "chapter_count": 13},
            {"title": "James", "slug": "JAS", "chapter_count": 5},
            {"title": "1 Peter", "slug": "1PE", "chapter_count": 5},
            {"title": "2 Peter", "slug": "2PE", "chapter_count": 3},
            {"title": "1 John", "slug": "1JN", "chapter_count": 5},
            {"title": "2 John", "slug": "2JN", "chapter_count": 1},
            {"title": "3 John", "slug": "3JN", "chapter_count": 1},
            {"title": "Jude", "slug": "JUD", "chapter_count": 1},
            {"title": "Revelation", "slug": "REV", "chapter_count": 22}]
    )


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
