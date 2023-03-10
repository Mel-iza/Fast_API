from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import numpy as np
import re
import json

from handlers.process_data import normalize_input_classes, get_one_value_from_class
from models.models import InputSentences

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


@app.post('/classes')
def get_input_classes(user_input: InputSentences):
  recomended_value = get_one_value_from_class(user_input.classes_do_user)
  print(recomended_value)
  return recomended_value



