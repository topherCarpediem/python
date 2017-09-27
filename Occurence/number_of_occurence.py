#Finding the number of occurence
s = "asdasdbobasdfsdfbobobasdbob"
key = "bob"
count = 0
for item in range(len(s)):
    if s[item:item+len(key)] == key:
        count += 1
print("Number of bob occurence: {}".format(count))

