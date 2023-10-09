# -*- coding: utf-8 -*-
"""English_2_HInglish.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zuOU6vG7iobH5IGz2q-glPqk3kprG9lN
"""

!pip install nltk
!pip install googletrans==4.0.0-rc1

import re
import nltk
from nltk import pos_tag, word_tokenize
from googletrans import Translator
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Function to find nouns in a sentence
def find_nouns(sentence):
    # Tokenize the sentence and get the part-of-speech tags
    words = word_tokenize(sentence)
    tags = pos_tag(words)

    # Extract nouns from the tagged words
    nouns = [word for word, tag in tags if tag in ['NN', 'NNS', 'NNP', 'NNPS']]

    return nouns

# Function to translate text to Hindi
def translate_to_hindi(text):
    translator = Translator()
    translation = translator.translate(text, src='en', dest='hi')
    return translation.text

# Function to replace nouns in Hindi sentence with their English counterparts
def replace_nouns_with_english(hindi_sentence, english_sentence):
    # Find nouns in the English sentence
    english_nouns = find_nouns(english_sentence)

    # Translate the English nouns to Hindi
    translated_nouns = [translate_to_hindi(noun) for noun in english_nouns]

    # Create a dictionary to map translated nouns to their English counterparts
    noun_mapping = {translated: original for original, translated in zip(english_nouns, translated_nouns)}

    # Replace nouns in the Hindi sentence with their English counterparts
    for hindi_noun, english_noun in noun_mapping.items():
        hindi_sentence = hindi_sentence.replace(hindi_noun, english_noun)

    return hindi_sentence

# Test the function
sentence = input("Enter a sentence: ")
hindi_translation = translate_to_hindi(sentence)

result_sentence = replace_nouns_with_english(hindi_translation, sentence)
print("Hinglish Sentence:", result_sentence)

# Input sentences
sentences = [
    "Definitely share your feedback in the comment section.",
    "So even if it's a big video, I will clearly mention all the products.",
    "I was waiting for my bag."
]

# Translate each sentence to Hinglish with word selection
for sentence in sentences:
  hindi_translation = translate_to_hindi(sentence)

  result_sentence = replace_nouns_with_english(hindi_translation, sentence)
  print("Hinglish Sentence:", result_sentence)

reference_translations = [
    "निश्चित रूप से comment section में अपनी feedback साझा करें।",
    "तो भले ही यह एक बड़ा video है, मैं स्पष्ट रूप से सभी products का उल्लेख करूंगा।",
    "मैं अपने बैग का इंतजार कर रहा था।"
]

# Initialize a counter for correct translations
correct_translations = 0

# Translate each sentence and compare to the reference translation
for sentence, reference in zip(sentences, reference_translations):
    hindi_translation = translate_to_hindi(sentence)
    result_sentence = replace_nouns_with_english(hindi_translation, sentence)

    # Check if the generated translation matches the reference translation
    if result_sentence == reference:
        correct_translations += 1

# Calculate accuracy
accuracy = (correct_translations / len(sentences)) * 100

# Print the accuracy
print(f"Accuracy: {accuracy:.2f}%")