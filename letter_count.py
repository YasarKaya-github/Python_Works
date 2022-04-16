sentence=input("Enter your sentence: ")
sentence_set=set()
for i in sentence:
    sentence_set.add(i)
result={}
for i in sentence_set:
    result[i]=sentence.count(i)
print(result)