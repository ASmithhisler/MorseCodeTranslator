import pandas
from art import logo


def encode(string, translation_list):
    first = True
    for word in string.split():
        if not first:
            translation_list.append(morse_code_dict[" "])
        first = False
        for char in word:
            try:
                translated_char = morse_code_dict[char]
            except KeyError:
                translated_char = morse_code_dict["Err"]
            translation_list.append(translated_char)
    return translation_list


def decode(string, translation_list):
    for code in string.split():
        try:
            translated_char = text_dict[code]
        except KeyError:
            translated_char = text_dict["#"]
        translation_list.append(translated_char)
    return translation_list


data = pandas.read_csv("morse_code.csv")
morse_code_dict = {row.char: row.code for (index, row) in data.iterrows()}
text_dict = {row.code: row.char for (index, row) in data.iterrows()}

print(logo)

retry = True
while retry == True:
    func = input("Type 'e' to encode, type 'd' to decode: ")
    string = input("Type your message: ").upper()

    translation_list = []
    if func == "e":
        translation_list = encode(string, translation_list)
    if func == "d":
        translation_list = decode(string, translation_list)

    translation = ""
    for char in translation_list:
        translation += char + " "

    print(f"The translation is: {translation}")

    restart = input("Type 'y' if you want to go again: ").lower()
    print()
    if restart == "y":
        retry = True
    else:
        retry = False
