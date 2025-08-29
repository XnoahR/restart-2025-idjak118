import csv
import copy

myBook = {
    "title" : "<empty>",
    "author": "<empty>",
    "pages" : 0,
    "release" : 0,
    "volume" :0,
    "price" :0
}

myBookList = []

with open('library.csv') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')
    lineCount = 0
    for row in csvReader:
        if lineCount == 0:
            print(f'column names are : {", ".join(row)}')
            lineCount += 1
        else:
            bookData = copy.deepcopy(myBook)
            bookData["title"] = row[0]
            bookData["artist"] = row[1]
            bookData["pages"] = row[2]
            bookData["release"] = row[3]
            bookData["volume"] = row[4]
            bookData["price"] = row[5]
            myBookList.append(bookData)
            lineCount+=1
    
    print(lineCount)
    print(myBookList)