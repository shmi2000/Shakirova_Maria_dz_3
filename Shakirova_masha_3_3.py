from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
list_1 = []


def get_jokes(n, flag=False):
    for i in range(n):
        random_index = choice(nouns)
        random_index_1 = choice(adverbs)
        random_index_2 = choice(adjectives)
        joke = "{} {} {}".format(random_index, random_index_1, random_index_2)
        print(joke)
        print(random_index)
        list_2 = []
        if flag == True:
            list_2 = joke.split()
            for i in range(len(nouns)):
                for fun in list_2:
                    if nouns[i] == fun:
                        nouns.pop(i)

        print(nouns)


get_jokes(3)
