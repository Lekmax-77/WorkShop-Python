def decorator_to_str(func):
    def inner(*args):
        return str(func(*args))
    return inner

@decorator_to_str
def add(a, b):
    return a + b

@decorator_to_str
def get_info(d):
    print(d['info'])
    return d['info']

# d = add(5, 30)
# get_info({'info': [1, 2, 3]})
