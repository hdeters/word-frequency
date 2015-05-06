def get_words(sentence):
    words = []
    new_words = []
    words = sentence.split()
    for word in words:
        new_word = word.strip(",!?.:;-")
        new_words.append(new_word)
    return new_words

def word_frequency(text):
    freq_dict = {}
    freq_dict2 = {}
    text = text.lower()
    clean_text = get_words(text)
    for word in clean_text:
        if word in freq_dict:
            freq_dict[word] += 1
        else:
            freq_dict[word] = 1

    sorted_dict = sorted(freq_dict.items(), key=lambda x:x[1], reverse=True)
    top_twenty = sorted_dict[0:20]

    for item in top_twenty:
        freq_dict2.update({ item[0] : item[1] })

    return freq_dict2

def print_word_frequency(thedict):
    newdict = sorted(thedict.items(), key=lambda x:x[1], reverse=True)
    for item in newdict:
        print(item[0] + "  " + str(item[1]))


if __name__=="__main__":
    sample = open("sample.txt")
    thedict = word_frequency(sample.read())
    print_word_frequency(thedict)
    sample.close()
