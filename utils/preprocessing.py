from typing import Any, List, Dict, Union

from pandas import isna
import html, re

def clean_text(text: str) -> str:
    """ Cleans string by removing unwanted characters """
    
    if not text or isna(text):
        return ""
    
    text = html.unescape(text) # Escape HTML Characters
    text = re.sub(r"\s+", " ", text).strip() # Removes extra whitespace
    
    return text

def remove_duplicates():
    """ Removes duplicates from data """

    pass