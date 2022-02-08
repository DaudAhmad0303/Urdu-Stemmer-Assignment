import  codecs
def stemmer(word = ''):
    # prefix
    # Rule 1
    if word[:2] == 'با':
        return word[2:], word[:2]
    # Rule 2
    if word[:2] == 'بے':
        return word[2:], word[:2]
    # Rule 3
    if word[:2] == 'پا':
        return word[2:], word[:2]
    # Rule 4
    if word[:2] == 'تہ':
        return word[2:], word[:2]
    # Rule 5
    if word[:2] == 'نا':
        return word[2:], word[:2]
    # Rule 6
    if word[:2] == 'پر':
        return word[2:], word[:2]
    # Rule 7
    if word[:2] == 'بد':
        return word[2:], word[:2]
    # Rule 8
    if word[:2] == 'ان':
        return word[2:], word[:2]
    # Rule 9
    if word[:2] == 'چو':
        return word[2:], word[:2]
    # Sufix
    # Rule 10
    if word[-2:] == 'تا':
        return word[:-2], word[-2:]
    # Rule 11
    if word[-2:] == 'تے':
        return word[:-2], word[-2:]
    # Rule 12
    if word[-2:] == 'نا':
        return word[:-2], word[-2:]
    # Rule 13
    if word[-2:] == 'یں':
        return word[:-2], word[-2:]
    # Rule 14
    if word[-3:] == 'یاں':
        return word[:-3], word[-3:]
    # Rule 15
    if word[-3:] == 'دار':
        return word[:-3], word[-3:]
    # Rule 16
    if word[-3:] == 'مند':
        return word[:-3], word[-3:]
    # Rule 17
    if word[-3:] == 'دار':
        return word[:-3], word[-3:]
    # Rule 18
    if word[-3:] == 'باز':
        return word[:-3], word[-3:]
    # Rule 19
    if word[-2:] == 'بر':
        return word[:-2], word[-2:]
    # Rule 20
    if word[-3:] == 'بین':
        return word[:-3], word[-3:]
    # Rule 21
    if word[-2:] == 'یا':
        return word[:-2], word[-2:]
    # Rule 22
    if word[-3:] == 'بار':
        return word[:-3], word[-3:]
    # Rule 23
    if word[-3:] == 'ںگے':
        return word[:-3], word[-3:]
    
    else: 
        return word, None




# ------------------        Driver Program      ----------------------

# tokens = dict()
words = []
stem = []
count = 0
f = codecs.open(r'D:\\Daud Ahmad\\6th Semester\\NLP\\Assignment\\input.txt','r','UTF-8')
# print(f.read())         # reading all file content
for x in f:
    lst = x.split()
    if len(lst) == 2:
        words.append(lst[0])
        stem.append(lst[1])
f.close()

f = codecs.open('Result.txt', 'w', 'UTF-8')
f.write('Words\t\tStem\t\tAffix\n')
for i in range(len(words)):
    f.write(words[i])
    f.write('\t\t')
    val , aff = stemmer(words[i])
    # print(val, aff)
    if val == stem[i]:
        count += 1
    f.write(val)
    f.write('\t\t')
    f.write(str(aff))
    f.write('\n')
# Accuracy 
print(f'Accuracy of given input is {(count/len(words)):%}')