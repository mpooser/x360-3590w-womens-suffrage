import nltk
nltk.download('punkt')
nltk.download('stopwords')
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

file2 = open("unbalanced/post-1920-books-unbl", 'r')
file1 = open("unbalanced/pre-1920-books-no-women-version-unbl", 'r')
#file2 = open("balanced/post_1920_books_bal", 'r')
#file1 = open("balanced/pre_1920_books_bal", 'r')

pre_text = file1.read()
post_text = file2.read()

file1.close()
file2.close()

# get those words
pre_tokens = word_tokenize(pre_text)
pre_tokens = [w.lower() for w in pre_tokens]
pre_table = str.maketrans('', '', string.punctuation)
pre_stripped = [w.translate(pre_table) for w in pre_tokens]
pre_words = [word for word in pre_stripped if word.isalpha()]

# get those words
post_tokens = word_tokenize(post_text)
post_tokens = [w.lower() for w in post_tokens]
post_table = str.maketrans('', '', string.punctuation)
post_stripped = [w.translate(post_table) for w in post_tokens]
post_words = [word for word in post_stripped if word.isalpha()]

# remove stopwords
stop_words = set(stopwords.words('english'))
pre_words = [w for w in pre_words if not w in stop_words]
post_words = [w for w in post_words if not w in stop_words]

# output words
pre_words_file = open('unbalanced/preprocessed_pre_1920_unbl.txt', 'w')
post_words_file = open('unbalanced/preprocessed_post_1920_unbl.txt', 'w')
#pre_words_file = open('balanced/preprocessed_pre_1920_bal.txt', 'w')
#post_words_file = open('balanced/preprocessed_post_1920_bal.txt', 'w')


for s in pre_words:
    pre_words_file.write(s)
    pre_words_file.write('\n')
    
for s in post_words:
    post_words_file.write(s)
    post_words_file.write('\n')

pre_words_file.close()
post_words_file.close()

##print(len(pre_words))
#print(len(post_words))

#fdist = nltk.FreqDist(pre_words)
#print(fdist['edna'])