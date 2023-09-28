import speech_recognition as sr
import nltk
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
from nltk.metrics import jaccard_distance
# Initialize the recognizer
recognizer = sr.Recognizer()
# Load an audio file (replace 'your_audio_file.wav' with the path to your audio file)
def get_pronouncation_text(audio_file):

# Open the audio file using the recognizer
  with sr.AudioFile(audio_file) as source:
    audio_data = recognizer.record(source)  # Record the entire audio file

# Use the Google Speech Recognition API to convert audio to text
  try:
    return True , recognizer.recognize_google(audio_data)
    print("Transcription: " + text)
  except sr.UnknownValueError:
    return False , "Could not understand the audio"
  except sr.RequestError as e:
    return False , "Could not request results; {0}"+format(e)

# Calculate Wu-Palmer Similarity using WordNet
def get_wordnet_similarity(word1 , word2):
  synset1 = wordnet.synsets(word1)[0]
  synset2 = wordnet.synsets(word2)[0]
  return wordnet.path_similarity(synset1, synset2, simulate_root=True)

def generate_words_in_sequence(letters):
    # Initialize a list to store words in sequence
    words_in_sequence = []

    # Generate words by progressively adding letters
    for i in range(1, len(letters) + 1):
      word = letters[:i]
      words_in_sequence.append(word)

    return words_in_sequence

def get_tokenize_word(word1 , word2):
  words1 = generate_words_in_sequence(word1)
  words2 = generate_words_in_sequence(word2)
  return words1 , words2
# from nltk.wup_similarity import wup_similarity

lemmatizer = WordNetLemmatizer()

def get_jaccard_similarity(word1 , word2):
  lemma1 = lemmatizer.lemmatize(word1, pos='v')  # 'run'
  lemma2 = lemmatizer.lemmatize(word2, pos='v')  # 'run'
  jaccard_similarity = 1 - jaccard_distance(set(lemma1), set(lemma2))
  return jaccard_similarity
# similarity_score = wordnet.path_similarity(synset1, synset2, simulate_root=True)
# print(similarity_score)
def get_tokenize_similarity(words1 , words2):
  total_similarity = 0
  comparisons = 0
  length = len(words2) if len(words1) >= len(words2) else len(words1)
  difference = len(words1) - len(words2) if len(words1) >= len(words2) else len(words2) - len(words1)
  for i in range(length):
    total_similarity+= get_jaccard_similarity(words1[i] , words2[i])
    comparisons+=1
  avg_similarity = total_similarity / (comparisons+difference)
  return avg_similarity

def get_pronouncation_accuracy(audio_file , pronounce_word):
  state , word1 = get_pronouncation_text(audio_file)
  if not state:
    print(word1)
    return
  word2 = pronounce_word
  print(word1 , word2)
  words1 , words2 = get_tokenize_word(word1 , word2)
  print(words1 , words2)
  tokenize_similarity = get_tokenize_similarity(words1 , words2)
  if tokenize_similarity>= 0.45:
    print('Hit Token Similarity')
    print('Pronouncation Accuracy = ',tokenize_similarity)
    return tokenize_similarity
  else:
    try:
      print('Hit Wordnet Similarity')
      wordnet_similarity = get_wordnet_similarity(word1 , word2)
      if wordnet_similarity>=0.45:
       print('Pronouncation Accuracy = ',wordnet_similarity)
       return wordnet_similarity
      else:
        print('Pronouncation Accuracy = ',0)
        return 0
    except:
      print('Hit jaccard Similarity')
      jaccard_similarity = get_jaccard_similarity(word1 , word2)
      print('Pronouncation Accuracy = ',jaccard_similarity)
      return jaccard_similarity

# audio_file = 'teacher2.wav'
# similarity = get_pronouncation_accuracy(audio_file , 'teachers')