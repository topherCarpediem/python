#Finding the number of vowel values
vowels = ["a", "e", "i", "o", "u"]
astring = 'tldhmmqpirueeiuiodcuyziv'
counter = 0
for item in astring:
    if item in vowels:
        counter = counter + 1
print("Number of vowels: {}".format(counter))


