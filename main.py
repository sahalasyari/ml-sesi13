# Ubah data teks menjadi lowercase
def to_lowercase(text):
    return text.lower()

# Contoh penggunaan
original_text = "This is an EXAMPLE Sentence."
updated_text = to_lowercase(original_text)
print(updated_text)  # output: "this is an example sentence."

# Hapus tanda baca
import string

def remove_punctuation(text):
    return text.translate(str.maketrans('', '', string.punctuation))

# Contoh penggunaan  
original_text = "Hello, World!"
updated_text = remove_punctuation(original_text)
print(updated_text)  # output: "Hello World"

# Hapus angka
import re

def remove_numbers(text):
    return re.sub(r'\d+', '', text)

# Contoh penggunaan
original_text = "There are 2 apples and 10 oranges."
updated_text = remove_numbers(original_text)
print(updated_text)  # output: "There are  apples and  oranges."

# Tokenisasi teks
from nltk.tokenize import word_tokenize # type: ignore
import nltk # type: ignore
nltk.download('punkt')

def tokenize(text):
    return word_tokenize(text)

# Contoh penggunaan
original_text = "This is an example sentence."
tokenized_text = tokenize(original_text)
print(tokenized_text)  # output: ['This', 'is', 'an', 'example', 'sentence', '.']

# Hapus stopwords
from nltk.corpus import stopwords # type: ignore
nltk.download('stopwords')

def remove_stopwords(words):
    stop_words = set(stopwords.words('english'))
    return [word for word in words if word not in stop_words]

# Contoh penggunaan
original_text = "This is an example showing stopwords removal."
tokenized_text = tokenize(original_text)
updated_text = remove_stopwords(tokenized_text)
print(updated_text)  # output: ['example', 'showing', 'stopwords', 'removal']

# Stemming kata-kata
from nltk.stem import PorterStemmer # type: ignore

def stem_words(words):
    ps = PorterStemmer()
    return [ps.stem(word) for word in words]

# Contoh penggunaan
original_text = "This is an example showing stemming of words."
tokenized_text = tokenize(original_text)
filtered_words = remove_stopwords(tokenized_text)
stemmed_words = stem_words(filtered_words)
print(stemmed_words)  # output: ['exampl', 'show', 'stem', 'word']

-------------------------------------------------------------------------------------

Hasil Output:

this is an example sentence.
Hello World
There are  apples and  oranges.
[nltk_data] Downloading package punkt to
[nltk_data]     C:\Users\febri\AppData\Roaming\nltk_data...
[nltk_data]   Package punkt is already up-to-date!
['This', 'is', 'an', 'example', 'sentence', '.']
[nltk_data] Downloading package stopwords to
[nltk_data]     C:\Users\febri\AppData\Roaming\nltk_data...
[nltk_data]   Package stopwords is already up-to-date!
['This', 'example', 'showing', 'stopwords', 'removal', '.']
['thi', 'exampl', 'show', 'stem', 'word', '.']
