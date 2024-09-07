# string = 'hello my best friend i really like spending time with you'

# result = ' '.join('£' + x.upper() for x in string.split() if len(x) >= 4)

# print(result)

string = 'hello my best friend i really like spending time with you'

# привести слова к upper и продублировать добавив ! в конец
# пример: hello --> HELLO! HELLO!

result = [x.upper() + '!' + ' ' + x.upper() + '!' for x in string.split()]

print(result)