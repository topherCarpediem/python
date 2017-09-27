# def exc():
#     num = input("number: ")
#     if float(num) < 0:
#         raise ValueError("Negative")
#
#
# exc()
#
# the_file = open("sample.txt", "w")
# the_file.writelines("Topher")
# the_file.close()

another = open("sample.txt", "r")
content = another.readline()
print(content)
another.close()


aanother = open("text.txt", "w")
aanother.write("Hello this is from hello.y")
print(content)
aanother.close()


squares = {1: 1, 2: 4, 3: 9, 4: 16, 8: 64}
print(squares)