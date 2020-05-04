import re

def make_text_block(dictionary):
    """Make text block form texts in dictionary of tweets."""
    separator = "   "
    text_block = separator.join(t['text'] for t in dictionary)
    text_block = re.sub(r'http\S+', '', text_block)
    # text_block = text_block[2]
    return text_block
