from collections import Counter
from itertools import chain

def load_text(path):
    f = open(path, 'r')
    text = [w.strip() for w in f.readlines()]
    f.close()
    #print(len(text))    
    return text


dictionary = ['mary', 'anne', 'alice', 'constance', 'eleanor',
              'catherine', 'elizabeth', 'mother', 'mom', 'wife', 'wench',
              'temptress', 'flapper', 'flap', 'moll', 'bearcat', 'housekeeper', 
              'caretaker', 'dorothy', 'edna', 'meredith', 'beth', 'sarah', 'sara', 
              'dina', 'rose', 'may', 'jane', 'esme', 'estee', 'victoria', 'olga',
              'eliza', 'abigail', 'eve', 'ruth', 'madame']

negative_dict = ['mistress','virago','frump','harridan','spinster','wench','slut','hooker','whore',
                 'tomboy','flapper','bitch', 'nasty', 'frump', 'harridan', 'matronly', 'mutton', 'shrill',
                 'spinster','witch','frail','kitten','looker']

roles_dict = ['housekeeper', 'caretaker', 'house', 'politics', 'nurse', 'cook', 'suffrage',
              'strike', 'war', 'reform', 'vote', 'factory', 'teacher', 'school', 'maid',
              'secretary', 'sewing', 'sewer']

presence_dict = ['flapper', 'flap', 'daughter', 'madame', 'mother', 'mom', 
                 'wife', 'girl', 'mary', 'anne', 'alice', 'constance', 'eleanor',
                 'catherine', 'elizabeth', 'wench', 'temptress', 'moll', 'bearcat',
                 'dorothy', 'edna', 'meredith', 'beth', 'sarah', 'sara', 'dina',
                 'rose', 'may', 'jane', 'esme', 'estee', 'victoria', 'olga', 'eliza',
                 'abigail', 'eve', 'ruth', 'angelic', 'spinster']


pre = load_text("unbalanced/preprocessed_pre_1920_unbl.txt")
post = load_text("unbalanced/preprocessed_post_1920_unbl.txt")
#pre = load_text("balanced/preprocessed_pre_1920_bal.txt")
#post = load_text("balanced/preprocessed_post_1920_bal.txt")
#print(pre[999])

#print(len(pre))
#print(len(post))

wordcount_pre = Counter(pre)
wordcount_post = Counter(post)



file = open("unbalanced/unbalanced_counts.txt", "w+")

print("pre")
file.write("--------------\n")
file.write("pre\n")
file.write("occupations\n")
file.write("--------------\n")
for f in wordcount_pre.items():
    if (f[0] in roles_dict):
        file.write(str(f))
        file.write('\n')
        
file.write("--------------\n")
file.write("presence\n")
for f in wordcount_pre.items():
    if (f[0] in presence_dict):
        file.write(str(f))
        file.write('\n')
        
file.write("--------------\n")
file.write("negative\n")
for f in wordcount_pre.items():
    if (f[0] in negative_dict):
        file.write(str(f))
        file.write('\n')
        
file.write("--------------\n")
print("post\n")
file.write("occupations\n")
file.write("--------------\n")
for f in wordcount_post.items():
    if (f[0] in roles_dict):
        print(f)
        file.write(str(f))
        file.write('\n')
        
file.write("--------------\n")
file.write("presence\n")

for f in wordcount_post.items():
    if (f[0] in presence_dict):
        print(f)
        file.write(str(f))
        file.write('\n')
        
file.write("--------------\n")
file.write("negative\n")
for f in wordcount_post.items():
    if (f[0] in negative_dict):
        file.write(str(f))
        file.write('\n')
        
file.close()

#print(len(wordcount_pre.items()))
#print(len(wordcount_post.items()))

print("Sums of each type from both datasets")
occupations_pre = 0
presence_pre = 0
negative_pre = 0
occupations_post = 0
presence_post = 0
negative_post = 0

for f in wordcount_pre.items():
    if (f[0] in roles_dict):
        occupations_pre += f[1]
    elif (f[0] in presence_dict):
        presence_pre += f[1]
    elif (f[0] in negative_dict):
        negative_pre += f[1]
        
for f in wordcount_post.items():
    if (f[0] in roles_dict):
        occupations_post += f[1]
    elif (f[0] in presence_dict):
        presence_post += f[1]
    elif (f[0] in negative_dict):
        negative_post += f[1]
        #print(f[1])
        
print("pre")
print(occupations_pre)
print(presence_pre)
print(negative_pre)
print("post")
print(occupations_post)
print(presence_post)
print(negative_post)
print(30*"*")
#print(f[])