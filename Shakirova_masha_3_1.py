def names(*args):
    my_list = {}
    for a in sorted(args):
        if a[0] not in my_list:
            my_list[a[0]] = list(filter(lambda element: element.startswith(a[:1]), args))
    print(my_list)


names("Винер", "Эмир", "Мария", "Елена", "Илхам", "Валентина")
