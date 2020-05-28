with open("i_have_a_dream.txt","r") as my_file:
    charNum=0
    wordNum=0
    lineNum=0
    while True:
        line = my_file.readline()
        if line.strip() != "":
            charNum += len(line)
            wordNum += len(line.split(" "))
            lineNum += 1
        if not line:
            break
        
    print(lineNum)
    print(charNum)
    print(wordNum)