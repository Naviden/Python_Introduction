import re

def text_cleaner(text):
    return re.sub('(^\W+|\W+$)', '', text)
    
