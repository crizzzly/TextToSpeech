#!/usr/bin/env python3.11
# Christina Rost, 2023-04
from io import BytesIO
import gtts
from playsound import playsound
from datetime import datetime
from pytz import timezone
import fitz  # for reading pdf
import pprint as pp


def text_to_speech(text, language='en', save_to_disk=False) -> None:
    """
    uses gtts library to convert text to speech in provided language.

    text: Text to convert to speech
    language: The language (IETF language tag) to read the text in. Default is en.
    save_to_disk: weather or not save created audio to disc. Default is False
    :param text: str
    :param language: str='en'
    :param save_to_disk: bool=False
    :return:
    """
    print("Converting text to speech")
    mp3_fp = BytesIO()
    # make request to google to get synthesis
    tts = gtts.gTTS(text, lang=language)

    # plays directly without saving - not working?
    # tts.write_to_fp(mp3_fp)
    print("saving.")
    filename = "1.mp3"  # datetime.now(tz=timezone("Europe/Berlin")).strftime("%Y-%m-%d_%H:%M") + ".pm3"
    tts.save(filename)
    playsound(filename)


def read_text_from_pdf(filename="books/Veronika.pdf"):
    """
    extracts text from a pdf file given in 'filename'.
    Defaults for testing purpose to a locally saved pdf file

    :param filename: str
    :return: str
    """
    # think of it:
    # https://rapidapi.com/collection/best-text-to-speech-apis
    print("reading pdf. \nContent:")
    text = ""
    doc = fitz.Document(filename)
    # get table of content
    toc = doc.get_toc()  # [<chapter>, <title>, <page+1>]


    # Check which page should be set to start read from to skip all those information in the first pages
    title = 'Veronika'
    start_page = 0
    for page in doc:
        page_dict = page.get_textpage().extractDICT()
        for block in page_dict['blocks']:
            for line in block['lines']:
                # print(f'l: {line}')
                for span in line['spans']:
                    if title in span['text']:
                        start_page = span['flags']
                        print(f'Start reading on page: {start_page}')
                        break

    # to_read = doc.pages(start_page, -1)
    to_read = doc.pages(52)
    txt = ''
    for page in to_read:
        txt += page.get_text()

    return txt


if __name__ == "__main__":
    # txt = read_text_from_pdf()
    # with open(f"extracted_pdf/python_coco_monty-{chapter}.html", "w") as f:
    #     f.write(html)
    # path_in = input("Please enter path to pdf file")
    # lang_in = input("Which language is pdf file? default: 'de'")
    text_to_speech(read_text_from_pdf('books/Coelho_Alchemist.pdf'), language='en')