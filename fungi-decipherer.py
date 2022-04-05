numcode=[]
wordcode=[]
while True:
    x=input("what is your number?")
    numcode.append(x)
    if x=="1":
        wordcode.append("a")
    elif x=="2":
        wordcode.append("b")
    elif x=="3":
        wordcode.append("c")
    elif x=="4":
        wordcode.append("d")
    elif x=="5":
        wordcode.append("e")
    elif x=="6":
        wordcode.append("f")
    elif x=="7":
        wordcode.append("g")
    elif x=="8":
        wordcode.append("h")
    elif x=="9":
        wordcode.append("i")
    elif x=="10":
        wordcode.append("j")
    elif x=="11":
        wordcode.append("k")
    elif x=="12":
        wordcode.append("l")
    elif x=="13":
        wordcode.append("m")
    elif x=="14":
        wordcode.append("n")
    elif x=="15":
        wordcode.append("o")
    elif x=="16":
        wordcode.append("p")
    elif x=="17":
        wordcode.append("q")
    elif x=="18":
        wordcode.append("r")
    elif x=="19":
        wordcode.append("s")
    elif x=="20":
        wordcode.append("t")
    elif x=="21":
        wordcode.append("u")
    elif x=="22":
        wordcode.append("v")
    elif x=="23":
        wordcode.append("w")
    elif x=="24":
        wordcode.append("x")
    elif x=="25":
        wordcode.append("y")
    elif x=="26":
        wordcode.append("z")
    elif x=="/":
        wordcode.append(" ")
    elif x=="done":
        fincode="".join(wordcode)
        print("your phrase is:",fincode)
        break
    else:
        print("invalid input")
    print(numcode)