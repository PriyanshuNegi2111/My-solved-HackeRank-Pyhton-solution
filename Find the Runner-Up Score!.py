if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    myList = []
    for item in arr:
        myList.append(item) 
    maxItem = max(myList)
    if myList.count(maxItem) != 1:  
        myList = list(dict.fromkeys(myList))    
    myList.remove(maxItem)
    print(max(myList))
