import pickle
string = input('Enter mail: ')

from nltk.stem import PorterStemmer
stemmer = PorterStemmer()

def stem_sentence(sentence):
    new=""
    for word in sentence.split(" "):
        new+=stemmer.stem(word.strip(',').strip('!').strip(' '))+" "
    return new

fm = open("E:\Study\OneDrive - Manipal Academy of Higher Education\Coding\Mini-Projects\Spam-Email-Detection\model\pickles\model_pickle",'rb')
model = pickle.load(fm)

fv = open("vectorizer_pickle",'rb')
vectorizer = pickle.load(fv)

string = stem_sentence(string)
print('\n\n',string)
check = vectorizer.transform([string])
print(model.predict(check)[0])

