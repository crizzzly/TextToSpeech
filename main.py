#!/usr/bin/env python3.11
# Christina Rost, 2023-04
from io import BytesIO
import gtts
from playsound import playsound
from datetime import datetime
from pytz import timezone


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
    mp3_fp = BytesIO()
    # make request to google to get synthesis
    tts = gtts.gTTS(text, lang=language)

    # plays directly without saving:
    tts.write_to_fp(mp3_fp)
    filename = "1.mp3"# datetime.now(tz=timezone("Europe/Berlin")).strftime("%Y-%m-%d_%H:%M") + ".pm3"
    tts.save(filename)
    playsound(filename)



if __name__ == "__main__":
    text_to_speech(" Nichts mach ich da", language='de')