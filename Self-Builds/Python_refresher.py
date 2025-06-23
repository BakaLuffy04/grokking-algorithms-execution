#find all prime numbers upto n
def primefinder(n):
    li=[]
    for i in range(2,n):
        if all(i % j != 0 for j in range(2, int(i**0.5)+1)):
            li.append(i)
    print (li)
primefinder(100)

#counting the frequency of words from a given string
def wordcount(line):
    line = line.lower()
    punctuation = '''!()-[]{};:\'",<>./?@#$%^&*_~'''
    clean_line = ''.join(i for i in line if i not in punctuation)
    arr= clean_line.split()
    count = {}
    for i in arr:
        if i in count:
            count[i] +=1
        else:
            count[i] =1
    print(count)
wordcount("Success is not final, failure is not fatal: it is the courage to continue that counts. Success requires consistency. Failure teaches lessons. And both are part of the journey.")

#Return squared even numbers from a list using filter() + lambda
def listfilter(num):
    new_num = list(filter(lambda x: x % 2 == 0, num))
    squared = list(map(lambda x: x**2, new_num))
    print(squared)
listfilter([1,2,3,4,5,6])
