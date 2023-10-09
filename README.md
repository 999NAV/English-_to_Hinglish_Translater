# English-_to_Hinglish_Translater

## 1. Import Necessary Libraries:
   - The code begins by importing the required libraries:
     - `re`: The `re` library is used for regular expressions but is not used in this code.
     - `nltk`: The Natural Language Toolkit (NLTK) library is used for natural language processing tasks such as tokenization and part-of-speech tagging.
     - `googletrans`: The `googletrans` library is used for translating text using the Google Translate API.

## 2. Download NLTK Data:
   - The code downloads necessary NLTK data by using `nltk.download()`. It specifically downloads the 'punkt' tokenizer and 'averaged_perceptron_tagger' data, which are required for tokenization and part-of-speech tagging.

## 3. Define Functions:
   - `find_nouns(sentence)`: This function tokenizes a given sentence, performs part-of-speech tagging to identify nouns (NN, NNS, NNP, NNPS), and returns a list of nouns found in the sentence.
   - `translate_to_hindi(text)`: This function uses the `googletrans` library to translate a given text from English (`src='en'`) to Hindi (`dest='hi'`) and returns the translated text.
   - `replace_nouns_with_english(hindi_sentence, english_sentence)`: This function replaces nouns in a Hindi sentence with their English counterparts. It does this by first finding nouns in the English sentence, translating them to Hindi, and then creating a mapping of translated nouns to their English counterparts. Finally, it replaces the nouns in the Hindi sentence using this mapping.

## 4. User Input and Testing:
   - The code prompts the user to input a sentence using `input()`. It then translates the input sentence to Hindi using the `translate_to_hindi` function and replaces nouns in the translated sentence with their English counterparts using the `replace_nouns_with_english` function. The result is printed as a "Hinglish Sentence."

## 5. Processing a List of Sentences:
   - A list of English sentences (`sentences`) is defined.
   - The code iterates through each sentence in the list, translates it to Hindi, and replaces nouns in the translated sentence with their English counterparts.
   - The resulting "Hinglish Sentence" is printed for each sentence in the list.

Overall, this code demonstrates how to use NLTK for tokenization and part-of-speech tagging, the Google Translate API for translation, and a custom function for replacing nouns in translated sentences. It's a basic example of working with natural language processing and translation tasks in Python.
