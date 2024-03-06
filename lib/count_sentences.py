#!/usr/bin/env python3
import re

class MyString:
    def __init__(self, value=''):
        if isinstance(value, str):
            self._value = value
        else:
            print("The value must be a string.")
            self._value = ''

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value):
        if isinstance(value, str):
            self._value = value
        else:
            print("The value must be a string.")

    def is_sentence(self):
        return self._value.endswith('.')

    def is_question(self):
        return self._value.endswith('?')

    def is_exclamation(self):
        return self._value.endswith('!')

    def count_sentences(self):
      
      words = self._value.split()
      sentences = [word for word in words if word.endswith(".") or word.endswith("!") or word.endswith("?")]
      return len(sentences)

    
        
       
        
        
    
   
s = MyString("Hello, world. Httieoue? Uieriuh. Grwiguiw!")
print(s.count_sentences())