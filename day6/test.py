book = {
    "harry potter" : "jk rowlings",
    "harry potter 2" : "jk rowlings",
    "harry potter 3" : "jk rowlings",
    "python" : "prasad",
    "java" : "sairam"
}


query = input()
search_list = []
for i in book:
    if query in i:
        search_list.append((i,book[i]))
    
if len(search_list) == 0:
    print("Query not found")
else:
    print(search_list)