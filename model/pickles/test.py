import pickle
import os
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()

def checkSpam(string):
    new=""
    for word in string.split(" "):
        new+=stemmer.stem(word.strip(' '))+" "
    
    fm = open(os.getcwd()+"\model\pickles\model_pickle",'rb')
    model = pickle.load(fm, encoding='latin1')
    fv = open(os.getcwd()+"\model\pickels\vectorizer_pickle",'rb')
    vectorizer = pickle.load(fv)

    check = vectorizer.transform([new])
    return model.predict(check)[0]

if __name__=='__main__':
    string = input('Enter mail: ')
    print(checkSpam(string))