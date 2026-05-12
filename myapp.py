import string
# allow the opening and reading of the files
with open("essay-1.txt", "r") as f:
    # convert the contents of the files to lowercase
    text1 = f.read().lower()

# allow the opening and reading of the files
with open("essay-2.txt", "r") as f:
    # convert the contents of the files to lowercase
    text2 = f.read().lower()

# remove punctuations
for p in string.punctuation:
    text1 = text1.replace(p, "")
    text2 = text2.replace(p, "")

# split the text into individual words
set1 = set(text1.split())
set2 = set(text2.split())

# finding common words in both files using intersection
common = set1 & set2
len1 = len(common)

# finding unique words from both essays
union = set1 | set2
len2 = len(union)

word1 = text1.split()
word2 = text2.split()

# ask the user to input a word
word = input("enter a word you would like to find: ")

count1 = word1.count(word)
count2 = word2.count(word)


# plagiarism percentage
plagiarism_percentage = (len1 / len2) * 100


def search_word(word):
    word = word.lower()
    return word in word1 or word in word2


print(search_word(word))


# Output result
print("common words: \n{}".format(", ".join(common)))
print()
print("unique words: \n{}".format(", ".join(union)))
print()
print("total number of comon words: ", (len1))
print()
print("total number of unique words is: ", (len2))
print()
print(f"Plagiarism Percentage: {plagiarism_percentage:.2f}%")
if plagiarism_percentage >= 50:
    print("plagiarism detected")
else:
    print("no plagiarism detected")
