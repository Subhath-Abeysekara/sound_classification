import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
nltk.download('stopwords')
nltk.download('punkt')
from nltk import pos_tag
nltk.download('averaged_perceptron_tagger')

def get_sentences_para(paragraph):
  sentences = sent_tokenize(paragraph)
  words = word_tokenize(paragraph)
# Get a list of English stopwords
  stop_words = set(stopwords.words('english'))

# Remove stopwords and punctuation
  filtered_words = [word.lower() for word in words if word.isalnum() and word.lower() not in stop_words]
  summarized_paragraph = ' '.join(filtered_words)
  print(summarized_paragraph)
  sentences = sent_tokenize(paragraph)
  print(sentences)
  return sentences

def generate_words_in_sequence(letters):
    # Initialize a list to store words in sequence
    words_in_sequence = []

    # Generate words by progressively adding letters
    for i in range(1, len(letters) + 1):
        word = letters[:i]
        words_in_sequence.append(word)

    return words_in_sequence

def get_pos_tags(sentence_):
  tokens = word_tokenize(sentence_)

# Perform part-of-speech tagging
  tagged_tokens = pos_tag(tokens)

# Extract POS tags into an array
  pos_tags = [tag for word, tag in tagged_tokens]
  return pos_tags

file1 = open('english_sentences.txt', 'r')
Lines = file1.readlines()
all_patterns = []
all_words_tokens = []
count = 0
# Strips the newline character
for line in Lines:
    pos_tags = get_pos_tags(line)
    words  = word_tokenize(line)
    count += 1
    print("Line{}: {}".format(count, line.strip()))
    print(generate_words_in_sequence(pos_tags))
    print(generate_words_in_sequence(words))
    all_patterns.append(generate_words_in_sequence(pos_tags))
    all_words_tokens.append(generate_words_in_sequence(words))

import pandas as pd
df = pd.read_csv('nounlist.csv')
print(list(df['nouns']))
nouns_list = list(df['nouns'])

def check_word_noun(word):
  if word in nouns_list:
    return True
  return False

def check_grammer(sentence):
  pos_tags = get_pos_tags(sentence)
  print(pos_tags)
  matching = False
  matching_sentence = ""
  i=0
  j=0
  for tags in all_patterns:
    word_token = all_words_tokens[i]
    j=0
    for pattern in tags:
      if all(element1 == element2 for element1, element2 in zip(pattern, pos_tags)) and len(pattern)==len(pos_tags):
        matching = True
        print(word_token)
        print(j)
        matching_sentence = word_token[j]
        break
      j+=1
    if matching:
      break
    i+=1
  return matching , matching_sentence

import re
from nltk.corpus import words
import itertools
nltk.download('words')
def has_number(word):
    # Define a regular expression pattern to match any digit (0-9)
    pattern = r'\d'

    # Use re.search to check if the pattern is found in the word
    if re.search(pattern, word):
        return True
    else:
        return False

def get_sentence(sentence):
  english_words = set(words.words())
  words_ = word_tokenize(sentence)
  meaning_full_words = []
  print(words)
  for word in words_:
    number = has_number(word)
    if word.lower() in english_words or number or check_word_noun(word):
      meaning_full_words.append(word)
  possible_sentences = []
  if len(words_)==len(meaning_full_words):
    print('perfect')
    return sentence
  matching , matching_sentence = check_grammer(sentence)
  if matching:
    return ' '.join(matching_sentence)
  permutations = list(itertools.permutations(meaning_full_words))

# Print the generated permutations
  i = 0
  for perm in permutations:
    sentence_ = ' '.join(perm)
    i+=1
    print(i)
    if i>= 10000:
      return sentence
    if check_grammer(sentence_):
      print(sentence_)
      return sentence_
  return sentence

def get_grammatical_sentence(sentences,sentence):
  for sentence in sentences:
    if check_grammer(sentence):
      print(sentence)
      return sentence
  return sentence

def create_para(sentences):
  print(sentences)
  return '.'.join(sentences)

def get_summerized_paragraph(paragraph):
  sentences = get_sentences_para(paragraph)
  best_sentences = []
  for sentence in sentences:
    best_sentence = get_sentence(re.sub(r'\.', '', sentence))
    best_sentences.append(best_sentence)
  summerized_para = create_para(best_sentences)
  print(summerized_para)
  return {
      "original" : paragraph,
      "summerized" : summerized_para
  }

# paragraph = "This is the john's book and it is very bla"
# get_summerized_paragraph(paragraph)