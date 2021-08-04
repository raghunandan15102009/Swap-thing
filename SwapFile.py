def swapText():
    with open('sample1.txt','r')as first:
        text_first= first.read()

    with open("sample2.txt",'r')as second:
        text_second=second.read()

    with open('sample1.txt','w')as first:
        first.write(text_second)

    print(text_first)


swapText()
