from random import choice, randrange

nouns = ["автомобиль", "лес", "огонь", "город", "дом", "пляж"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью", "утром", "два дня назад"]
adjectives = ["веселый", "яркий", "зеленый", "кожанный", "утопичный", "мягкий"]


def get_jokes(n, repeat=False):
    for i in range(n):
        random_index = choice(nouns)
        random_index_1 = choice(adverbs)
        random_index_2 = choice(adjectives)
        joke = "{} {} {}".format(random_index, random_index_1, random_index_2)
        print(joke)


get_jokes(1)
