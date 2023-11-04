import pytesseract
import PIL.Image
import dictionary_class
import tkinter as tk
from googletrans import Translator, LANGUAGES
from functools import partial


pyt_config = "--psm 6 --oem 3"
lang_engl = "en"
lang_span = "es"


def string_to_word_list(string) -> list:
    word_list = string.split()
    return word_list


def translate_unknown_word(translator, unknown_word, dest_lang):
    translated_result = translator.translate(unknown_word, dest=dest_lang)
    translated_text = translated_result.text
    return translated_text


def get_text_from_img(img, lang) -> list:
    text = pytesseract.image_to_string(PIL.Image.open(img), config=pyt_config)
    word_list = string_to_word_list(text)
    return word_list

def word_clicked(event, word_list, lang, translator):
    label = event.widget
    word_index = label.index(tk.END)
    word = label.get(1.0, tk.END)  # Retrieve the word from the label's text
    translated_word = translate_unknown_word(translator, word, lang)
    print(translated_word)
    label.delete(1.0, tk.END)  # Clear the label's current text
    label.insert(tk.END, translated_word)  # Insert the translated word
    label.config(width=len(translated_word))

def add_words_to_gui(root, word_list, lang, translator):
    for index, word in enumerate(word_list):
        label = tk.Text(root, wrap=tk.WORD, height=1, width=len(word))
        label.insert(tk.END, word)  # Insert the original word
        label.grid(row=0, column=index, padx=5, pady=5)
        label.bind("<Button-1>", partial(word_clicked, word_list=word_list, lang=lang, translator=translator))


if __name__ == "__main__":
    root = tk.Tk()
    root.title("balls")
    translater = Translator()

 # List of words
    word_list = ["Word1", "Word2", "Word3", "Word4"]

 # Add words to the GUI
    add_words_to_gui(root, word_list, lang_span, translater)

 # Start the GUI main loop
    root.mainloop()