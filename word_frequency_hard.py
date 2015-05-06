import sys

ignore_string = """a,able,about,across,after,all,almost,also,am,among,an,and,any,are,as,at,be,
because,been,but,by,can,cannot,could,dear,did,do,does,either,else,ever,every,
for,from,get,got,had,has,have,he,her,hers,him,his,how,however,i,if,in,into,is,
it,its,just,least,let,like,likely,may,me,might,most,must,my,neither,no,nor,
not,of,off,often,on,only,or,other,our,own,rather,said,say,says,she,should,
since,so,some,than,that,the,their,them,then,there,these,they,this,tis,to,too,
twas,us,wants,was,we,were,what,when,where,which,while,who,whom,why,will,with,
would,yet,you,your"""

newstring = ""

for x in ignore_string:
    if x != "\n":
        newstring = newstring + x

ignore_list = newstring.split(",")


def get_words(file_text):
    words = []
    new_words = []
    words = file_text.split()
    for word in words:
        new_word = word.strip(",!?\"\n.:;-")
        new_words.append(new_word)
    return new_words

def word_frequency(text):
    freq_dict = {}
    freq_dict2 = {}
    sorted_dict2 = []
    text = text.lower()
    clean_text = get_words(text)
    for word in clean_text:
        if word in freq_dict:
            freq_dict[word] += 1
        else:
            freq_dict[word] = 1

    sorted_dict = sorted(freq_dict.items(), key=lambda x:x[1], reverse=True)

    #Take common words out
    for item in sorted_dict:
        if item[0] not in ignore_list:
            sorted_dict2.append(item)

    top_twenty = sorted_dict2[0:20]

    for item in top_twenty:
        freq_dict2.update({ item[0] : item[1] })

    return freq_dict2

def print_word_frequency(thedict):
    newdict = sorted(thedict.items(), key=lambda x:x[1], reverse=True)
    number_of_occurences = 0
    for item in newdict:
        no_of_spaces = 13 - len(item[0])
        number_of_occurences = int(item[1] // 6.9)

        print("\n" + item[0], end="")


        while no_of_spaces > 0:
            print(" ", end="")
            no_of_spaces -= 1

        print(number_of_occurences, end="")
        print("  ", end="")

        while number_of_occurences > 0:
            print("#", end="")
            number_of_occurences -= 1

    print("\n")


if __name__=="__main__":
    if len(sys.argv) > 1:
        print ("Input only one file, Using the first file")
        filename = sys.argv[1]
    else:
        filename = sys.argv[1]
    sample = open(filename)
    thedict = word_frequency(sample.read())
    print_word_frequency(thedict)
    sample.close()
