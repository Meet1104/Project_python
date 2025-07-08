def filter_args(*args):
    strings = [x for x in args if isinstance(x, str)]
    numbers = [x for x in args if isinstance(x, (int, float))]
    return strings, numbers

print(filter_args("John", 25, "Doe", 12.5, "AI"))
