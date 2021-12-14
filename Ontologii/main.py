import nltk


def noun_verb_noun(sentence):
    sentence = nltk.word_tokenize(sentence)
    tagged_words = nltk.pos_tag(sentence)
    noun1 = False
    verb = False
    noun2 = False
    for i in range(len(tagged_words)):
        if (tagged_words[i])[1] == 'NN' and not noun2 and not verb:
            noun1 = True
        if (tagged_words[i])[1] == 'VB' and noun1 and not noun2:
            verb = True
        if (tagged_words[i])[1] == 'NN' and noun1 and verb:
            noun2 = True
    return noun1 and verb and noun2


if __name__ == '__main__':
    f = open("computer-science.txt", "r", encoding="utf8")
    g = open('noun_verb_noun.txt', 'a', encoding="utf8")
    text = f.read()
    sentences = nltk.sent_tokenize(text)
    for sentence in sentences:
        if noun_verb_noun(sentence):
            g.write(sentence + '\n')
    f.close()
    g.close()
