import pandas as pd
import numpy as np
import re
import re
import json
import sys 
sys.path.insert(1, '..')


def normalize_input_classes(userInput):
  first_input = json.dumps(userInput)
  converted_input = json.loads(first_input)
  
  texts = converted_input.values()
  texts = str(list(userInput))
  texts = texts.replace('[', '')\
             .replace(']', '')\
             .replace('ç', 'c')\

  texts = re.sub(r'(@[A-Za]+)|([^A-Za-z \t])|(\w+:\/\/\S+)|^.', ' ', texts)           
  texts = texts.lower()
  texts = texts.split()

  return texts
  

def get_one_value_from_class(userInput):
  input_classes = normalize_input_classes(userInput)

  for index, item in enumerate(userInput.keys()):
    for index, text in enumerate(input_classes):
      if (str(item) == str(text)):
        first_value = text
  return first_value