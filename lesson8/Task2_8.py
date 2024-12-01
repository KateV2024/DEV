# Создать декоратор

def typed(type):
    def decorator(func):
        def wrapper(*args, **kwargs):
            new_args = []

            if type == "str":
                check_type = str
            elif type == "int":
                check_type = int
            elif type == "float":
                check_type = float

            for arg in args:
                if isinstance(arg, check_type):
                    new_args.append(arg)
                else:
                    new_args.append(check_type(arg))

            return func(*new_args, **kwargs)
        return wrapper
    return decorator

@typed(type="str")
def foo_str(*args, **kwargs):
    return "".join(args)

print(foo_str("3", 5))  # "35"
print(foo_str(5, 5))  # "55"
print(foo_str("a", "b"))  # "ab"

@typed(type="float")
def foo_float(*args, **kwargs):
    return sum(args)

print(foo_float(5, 6, 7))  # 18.0
print(foo_float("3", 5, 0))  # 8.0
print(foo_float(0.1, 0.2, 0.3))  # 0.6
