import nltk

if __name__ == '__main__':
    f = open("test.txt", "r")
    text = f.read()
    split_text = nltk.sent_tokenize(text)
    print(split_text[0])

