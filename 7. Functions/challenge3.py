# Challenge:

# Solution
import re
from collections import Counter
def word_count(text):
  return len(text.split())

def char_count(text):
  return len(text.replace(" ", ""))

def sentence_count(text):
  sen_count = len(re.findall(r'[.?!]+', text))
  return sen_count

def avg_word_length(text):
  words = text.split()
  total_letters = 0
  total_words = len(words)
  for word in words:
    total_letters += len(word)
  word_length = round(total_letters / total_words, 1)

  return word_length

def common_word_find(text):
  words = text.lower().split()
  counts = Counter(words)

  most_common = counts.most_common(1)
  return most_common[0][0]

def longest_word_find(text):
  words = text.split()
  longest_word = ""
  for word in words:
    if len(word) > len(longest_word):
      longest_word = word

  return longest_word

def text_analyzer(text):
  print(f"Words Count: {word_count(text)}")
  print(f"Characters count: {char_count(text)}")
  print(f"Sentences Count: {sentence_count(text)}")
  print(f"Average word length: {avg_word_length(text)}")
  print(f"Most common word: {common_word_find(text)}")
  print(f"Longest word: {longest_word_find(text)}")

text = "Hey I am Atif Zafar from Aligarh. I am studying in Aligarh Muslim University."
print(f"Text: {text}")
text_analyzer(text)
