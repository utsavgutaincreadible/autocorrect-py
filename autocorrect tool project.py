
BharatIntern - Task 1
Building an *AUTO-CORRECTION* tool using AI in Python


pip install spello
     
Requirement already satisfied: spello in /usr/local/lib/python3.10/dist-packages (1.3.0)
Requirement already satisfied: nltk<4,>=3.4.5 in /usr/local/lib/python3.10/dist-packages (from spello) (3.8.1)
Requirement already satisfied: click in /usr/local/lib/python3.10/dist-packages (from nltk<4,>=3.4.5->spello) (8.1.6)
Requirement already satisfied: joblib in /usr/local/lib/python3.10/dist-packages (from nltk<4,>=3.4.5->spello) (1.3.1)
Requirement already satisfied: regex>=2021.8.3 in /usr/local/lib/python3.10/dist-packages (from nltk<4,>=3.4.5->spello) (2022.10.31)
Requirement already satisfied: tqdm in /usr/local/lib/python3.10/dist-packages (from nltk<4,>=3.4.5->spello) (4.65.0)

from spello.model import SpellCorrectionModel
     

sp = SpellCorrectionModel(language="en")
     

with open ("words.txt") as file:
    data = file.readlines()

data = [i.strip() for i in data]
     

sp.train(data)
     
Spello training started..
DEBUG:spello.settings:Spello training started..
Context model training started ...
DEBUG:spello.settings:Context model training started ...
Symspell training started ...
DEBUG:spello.settings:Symspell training started ...
Phoneme training started ...
DEBUG:spello.settings:Phoneme training started ...
Spello training completed successfully ...
DEBUG:spello.settings:Spello training completed successfully ...

sp.save("")
     
'./model.pkl'

sp.load("model.pkl")
     
<spello.model.SpellCorrectionModel at 0x7d820801b280>

sentence = input("Enter the sentence/word : ")
     
Enter the sentence/word : Acheive

words = sentence.split()
     

correct_words = []
for word in words:
    corrected = sp.spell_correct(word)
    correct_words.append(corrected['spell_corrected_text'])

corrected_sentence = " ".join(correct_words)
     
DEBUG:spello.settings:Symspell suggestions: [('achieve', 1), ('achieve', 1), ('achieve', 1)]
DEBUG:spello.settings:Phoneme suggestions: [('achieve', 1), ('achieve', 1), ('achieve', 1), ('acer', 4), ('acre', 4), ('acre', 4)]
DEBUG:spello.settings:Suggestions dict from phoneme and symspell are: {'acheive': ['achieve', 'acer', 'acre']}
DEBUG:spello.settings:text after context model: achieve
DEBUG:spello.settings:Spell-correction Results {'original_text': 'Acheive', 'spell_corrected_text': 'achieve', 'correction_dict': {'Acheive': 'achieve'}}

corrected_sentence
     
'achieve'