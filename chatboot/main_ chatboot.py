from newspaper import Article
import random
import string
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_distances
import numpy as np

#pobrane paczki punkt


nltk.download('punkt', quiet=True)
article = Article('https://www.mayoclinic.org/diseases-conditions/chronic-kidney-disease/symptoms-causes/syc-20354521')
article.download()
article.parse()
article.nlp()

corpus = article.text

#print(corpus)

# Tokenizacja

text = corpus

sentence_list = nltk.sent_tokenize(text)



def greeting_res(text):
    text = text.lower()
    bot_greeting = ['hello', 'hi', 'hello']
    user_greeting = ['hi', 'hey', 'holla', 'greetings', 'wassup']
    for word in text.split():
        if word in user_greeting:
            return random.choice(bot_greeting)


#function to sort values
def index_sort(list_var):
    length = len(list_var)
    list_index = list(range(0, length))
    x = list_var
    for i in range(length):
        for j in range(length):
            if x[list_index[i]] > x[list_index[j]]:
                #swap
                temp = list_index[i]
                list_index[i] = list_index[j]
                list_index[j] = temp
    return list_index
#eaziest way to take bigest value is
def index_sort2(list_var):
    sorted(list_var, reverse=True)


def response_bot(user_input):
    user_input = user_input.lower()
    sentence_list.append(user_input)
    bot_response = ''
    cm = CountVectorizer().fit_transform(sentence_list)
    similarity_scores = cosine_distances(cm[-1], cm)
    similarity_scores_list = similarity_scores.flatten()
    index = index_sort2(similarity_scores_list)
    index = index[1:0]
    response_flag = 0

    j = 0
    for i in range(len(index)):
        if similarity_scores_list[index[1]] > 0.0:
            bot_response = bot_response + " " + sentence_list[index[i]]
            response_flag = 1
            j = j + 1
        if j > 2:
            break
    if response_flag == 0:
        bot_response = bot_response + " " + "I Dont understand"
    sentence_list.remove(user_input)
    return bot_response
print("im a doctor a will health you please insert")


exit_list = ['exit', 'bye', 'break']
while(True):
    user_input = input()
    if user_input.lower() in exit_list:
        print('Doc chatbootbye ')
        break
    else:
        if greeting_res(user_input) != None:
            print('Doc Bot: ' + greeting_res(user_input))







# user_input = "hi world"
# sentence_list.append(user_input)
# bot_response = ''
# cm = CountVectorizer().fit_transform(sentence_list)
# similarity_scores = cosine_distances(cm[-1], cm)
# similarity_scores_list = similarity_scores.flatten()
# index = index_sort(similarity_scores_list)
#
# print(similarity_scores_list)
# print(index)