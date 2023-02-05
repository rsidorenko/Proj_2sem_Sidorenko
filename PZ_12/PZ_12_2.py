words = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. " \
        "Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. " \
        "Donec quam felis, ultricies nec"


def str_lower(lower):
    for i in lower:
        yield i.lower()


words_lower = ''.join(str_lower(words))
print(words_lower)
