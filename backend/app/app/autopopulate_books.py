# from docx import Document

# doc = Document("Fresh Word (Full Version).docx")
# paragraphs = (doc.paragraphs)

# books = ['Genesis', 'Exodus', 'Leviticus', 'Numbers', 'Deuteronomy', 'Joshua', 'Judges', 'Ruth', '1 Samuel', '2 Samuel', '1 Kings', '2 Kings', 'Ezekiel', '1 Chronicles', '2 Chronicles', 'Ezra', 'Nehemiah', 'Esther', 'Job', 'Psalms', 'Proverbs', 'Ecclesiastes', 'Song of Solomon', 'Isaiah', 'Jeremiah', 'Lamentations', 'Daniel', 'Hosea', 'Joel', 'Amos', 'Obadiah', 'Jonah', 'Micah',
#          'Nahum', 'Habakkuk', 'Zephaniah', 'Haggai', 'Zechariah', 'Malachi', 'Matthew', 'Mark', 'Luke', 'John', 'Acts', 'Romans', '1 Corinthians', '2 Corinthians', 'Galatians', 'Ephesians', 'Philippians', 'Colossians', '1 Thessalonians', '2 Thessalonians', '1 Timothy', '2 Timothy', 'Titus', 'Philemon', 'Hebrews', 'James', '1 Peter', '2 Peter', '1 John', '2 John', '3 John', 'Jude', 'Revelation']


# # cleaning for ezekial -- has number that are not chapter - Ezekiel removed
# chapters = []


# def get_chapters_dict():
#     chapter_dict = {}
#     prev_chapter = None
#     prev_chapter_index = 1

#     for book_name in books:
#         for idx, paragraph in enumerate(paragraphs):
#             if paragraph.text.startswith(book_name):
#                 chapters.append(paragraph.text)
#                 new_chapter = paragraph.text
#                 new_chapter_index = idx  # save pos

#                 if prev_chapter == None:
#                     prev_chapter = new_chapter
#                     continue

#                 if new_chapter != prev_chapter:
#                     chapter_dict[prev_chapter] = get_chapter_text(
#                         start_index=prev_chapter_index,
#                         stop_index=new_chapter_index)

#                     # move to the next chapter
#                     prev_chapter = new_chapter
#                     prev_chapter_index = new_chapter_index + 1

#     # For the very last one i.e Revelation 22
#     chapter_dict[prev_chapter] = get_chapter_text(
#         start_index=prev_chapter_index,
#         stop_index=len(paragraphs))

#     return chapter_dict


# def get_chapter_text(start_index, stop_index):
#     text = map(
#         lambda paragraph: paragraph.text,
#         paragraphs[start_index:stop_index])

#     return ' '.join(list(text))


# result = get_chapters_dict()
