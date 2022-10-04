from utils_formacion.math import list_operations
from utils_formacion.string import preprocessing

input_text = "Be not afraid of greatness. Some are born great, some achieve greatness, and others have greatness thrust upon them."

list_unique_words = preprocessing.get_unique_words(input_text)
nbr_unique_words = list_operations.get_list_length(list_unique_words)

print(f"This is the raw text: {input_text}")
print(f"This is our clean list of unique words: {list_unique_words}")
print(f"It contains {nbr_unique_words} elements.")