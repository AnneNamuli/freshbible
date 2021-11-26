from backend.models.db_models import Bible_Chapter, Bible_Verse
from backend.db.session import SessionLocal
import logging
import os


from docx import Document

path = os.path.abspath("FreshWord.docx")

doc = Document(path)
paragraphs = (doc.paragraphs)


books = ['Genesis', 'Exodus', 'Leviticus', 'Numbers', 'Deuteronomy', 'Joshua', 'Judges', 'Ruth', '1 Samuel', '2 Samuel', '1 Kings', '2 Kings', 'Ezekiel', '1 Chronicles', '2 Chronicles', 'Ezra', 'Nehemiah', 'Esther', 'Job', 'Psalms', 'Proverbs', 'Ecclesiastes', 'Song of Solomon', 'Isaiah', 'Jeremiah', 'Lamentations', 'Daniel', 'Hosea', 'Joel', 'Amos', 'Obadiah', 'Jonah', 'Micah',
         'Nahum', 'Habakkuk', 'Zephaniah', 'Haggai', 'Zechariah', 'Malachi', 'Matthew', 'Mark', 'Luke', 'John', 'Acts', 'Romans', '1 Corinthians', '2 Corinthians', 'Galatians', 'Ephesians', 'Philippians', 'Colossians', '1 Thessalonians', '2 Thessalonians', '1 Timothy', '2 Timothy', 'Titus', 'Philemon', 'Hebrews', 'James', '1 Peter', '2 Peter', '1 John', '2 John', '3 John', 'Jude', 'Revelation']

db = SessionLocal()
bible_chapter = db.query(Bible_Chapter)

bible_verse = db.query(Bible_Verse).first()  # check if Verse table has data


def get_chapters_dict():
    chapter_dict = {}
    prev_chapter = None
    prev_chapter_index = 1

    for book_name in books:
        for idx, paragraph in enumerate(paragraphs):
            if paragraph.text.startswith(book_name):
                new_chapter = paragraph.text
                new_chapter_index = idx  # save pos

                if prev_chapter == None:
                    prev_chapter = new_chapter
                    continue

                if new_chapter != prev_chapter:
                    chapter_dict[prev_chapter] = get_chapter_text(
                        start_index=prev_chapter_index,
                        stop_index=new_chapter_index)

                    # move to the next chapter
                    prev_chapter = new_chapter
                    prev_chapter_index = new_chapter_index + 1

    # For the very last one i.e Revelation 22
    chapter_dict[prev_chapter] = get_chapter_text(
        start_index=prev_chapter_index,
        stop_index=len(paragraphs))

    return chapter_dict


def get_chapter_text(start_index, stop_index):
    text = map(
        lambda paragraph: paragraph.text,
        paragraphs[start_index:stop_index])

    return ' '.join(list(text))


result = get_chapters_dict()


def get_verses():
    output = []

    if bible_verse:
        logging.info('Verses are already populated in the database')
        pass

    else:
        for row in bible_chapter:

            data = row.__dict__
            output.nd({data['id']: data['title']})

        for data in output:

            [[chapter_id, chapter]] = data.items()

            try:
                chapter_str = result[chapter]
            except KeyError:
                continue

            chapter_num = [int(word)
                           for word in chapter_str.split() if word.isdigit()]

            if chapter_num:
                verse_range = range(1, chapter_num[-1]+1)

                logging.info('Writing verses to the database')

                for i in range(len(verse_range)):

                    if i < len(verse_range)-1:
                        try:
                            verse = chapter_str[chapter_str.index(
                                str(verse_range[i])):chapter_str.index(str(verse_range[i+1]))].replace('\u200b', '')

                            verse_num = [int(word)
                                         for word in verse.split() if word.isdigit()]

                            if len(verse_num) == 1:
                                db_obj = {'chapter_id':  chapter_id,
                                          'chapter': chapter,
                                          'verse_number': verse_num[0],
                                          'text': verse
                                          }

                                verse_data = Bible_Verse(**db_obj)

                                db.add(verse_data)
                                db.commit()

                        except ValueError:
                            pass

                    else:

                        try:
                            verse = chapter_str[chapter_str.index(
                                str(verse_range[-1])):].replace('\u200b', '')
                            verse_num = [int(word)
                                         for word in verse.split() if word.isdigit()]
                            logging.info('Writing verses to the database')

                            if len(verse_num) == 1:
                                db_obj = {'chapter_id':  chapter_id,
                                          'chapter': chapter,
                                          'verse_number': verse_num[0],
                                          'text': verse
                                          }

                                verse_data = Bible_Verse(**db_obj)

                                db.add(verse_data)
                                db.commit()

                        except ValueError:
                            pass

            logging.info('Done! Verses table populated')
