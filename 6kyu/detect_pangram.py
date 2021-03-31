# A pangram is a sentence that contains every single letter of the alphabet at least once. 
# For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, 
# because it uses the letters A-Z at least once (case is irrelevant).

# Given a string, detect whether or not it is a pangram. Return True if it is, False if not. 
# Ignore numbers and punctuation.

import string

def is_pangram(s):
  s2 = ''; match = 'abcdefghijklmnopqrstuvwxyz';
  
  for char in s:
    if char.lower() in match and char not in s2:
      s2 += char.lower()

  return True if ''.join(sorted(s2)) == match else False