def fileWordCount():
    fileName=input("Enter a file name")
    f=open(fileName)
    count=0
    lines=f.readlines()
    for i in lines:
        
        words=i.split()
        count+=len(words)
    print(count)

fileWordCount()