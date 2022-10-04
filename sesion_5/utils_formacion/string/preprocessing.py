from typing import List

def clean_string(text:str)->str:
    """Cleans an input text by applying the following steps:
    - strip
    - lowercase

    Parameters
    ----------
    text : str
        input raw text

    Returns
    -------
    str
        cleaned string
    """
    clean_str = str(text).strip().lower()
    return clean_str

def get_unique_words(
    text:str,
    sep=" ",
    chars_to_remove:List=[",","."]
    )->List:
    """Returns a list of unique words from input text.
    Applies a clean text function (strip/lowercase) to all words. 

    Parameters
    ----------
    text : str
       Input text
    sep : str, optional
        Separator to be used as reference for splitting words
    chars_to_remove : List, optional
        List of characters to be removed. 

    Returns
    -------
    List
        List of unique words based on input text
    """
    # Remove chararcters
    for c in chars_to_remove:
        text = str(text).replace(c,sep)

    # split based on sep
    words_list = text.split(sep)

    # clean words
    clean_list = []
    for w in words_list:
        clean_list.append(clean_string(w))

    # unique words
    unique_words = list(set(clean_list))

    return unique_words