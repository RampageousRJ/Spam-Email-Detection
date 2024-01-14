import pickle
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()

def checkSpam(string):
    new=""
    for word in string.split(" "):
        new+=stemmer.stem(word.strip(' '))+" "
    
    fm = open("E:\Study\OneDrive - Manipal Academy of Higher Education\Coding\Mini-Projects\Spam-Email-Detection\model\pickles\model_pickle",'rb')
    model = pickle.load(fm)
    fv = open("vectorizer_pickle",'rb')
    vectorizer = pickle.load(fv)

    check = vectorizer.transform([new])
    return model.predict(check)[0]

if __name__=='__main__':
    string = input('Enter mail: ')
    print(checkSpam(string))