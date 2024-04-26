heterElementsList = ["hello world", 69, 'xyz', 42.0, '88', 420, 88]
filteredList = []
for i in heterElementsList:
    if isinstance(i,int):
        filteredList.append(i)
print(filteredList)
