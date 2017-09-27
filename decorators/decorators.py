def decor(func):
    def warp():
        print("===========================")
        func()
        print("===========================")
    return warp


@decor
def print_text():
    print("Hi i am christopher")


print_text()
