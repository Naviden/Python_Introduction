import re

def text_cleaner(text):
    return re.sub('(^\W+|\W+$)', '', text)
    
def text_splitter(text):
    text = text_cleaner(text)
    return text.split()