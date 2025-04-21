import pandas

data = pandas.read_csv("morse_code.csv")
morse_code_dict = {row.char: row.code for (index, row) in data.iterrows()}

string = input("Type your message: ").upper()
translation_list = []

for word in string.split():
    for char in word:
        try:
            translated_char = morse_code_dict[char]
        except KeyError:
            translated_char = morse_code_dict["Err"]
        translation_list.append(translated_char)
    translation_list.append(morse_code_dict[" "])

translation = ""
for char in translation_list:
    translation += char + " "

print(f"The translation is: {translation}")
