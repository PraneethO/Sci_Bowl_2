import json

# subject, type (1 for Toss Up), MC_SA (Short or Multiple), Question, W:, X:, Y:, Z:, Answer: ___ (Letter for MC)

f = open("raw_text/Biology.txt", "r")
final = "{"
temp = "{\"subject\":\"Biology\", "

for line in f:
    if(line=="TOSS-UP \n"):
        temp += "\"type\": 1, \"MC_SA\": "
    elif(line=="BONUS \n"):
        temp += "\"type\": 2, \"MC_SA\": "
    
    if(line[0].isdigit()):
        line_list = line.split()
        temp += "\"" + line_list[2] + "\", \"Question\": \""
        for i in range(4, len(line_list)):
            temp += line_list[i] + " "       
       
    if((not line[0].isupper()) and (not line == "------------------------------------------------------------------------------------------\n") and (not line == " \n") and (not line[1] == ")")):
        temp += line[:-2] + "\""
        
    if(line[:2] == "W)"):
        temp += ", \"W\": \""
        for i in range(1, len(line.split())-1):
            temp += line.split()[i] + " "
        temp += line.split()[-1]
        temp += "\""
        
    if(line[:2] == "X)"):
        temp += ", \"X\": \""
        for i in range(1, len(line.split())-1):
            temp += line.split()[i] + " "
        temp += line.split()[-1]
        temp += "\""
        
    if(line[:2] == "Y)"):
        temp += ", \"Y\": \""
        for i in range(1, len(line.split())-1):
            temp += line.split()[i] + " "
        temp += line.split()[-1]
        temp += "\""
        
    if(line[:2] == "Z)"):
        temp += ", \"Z\": \""
        for i in range(1, len(line.split())-1):
            temp += line.split()[i] + " "
        temp += line.split()[-1]
        temp += "\""
        
    if(line[:7] == "ANSWER:"):
        temp += ", \"Answer\": \""
        
        if(line.split()[1][0]=="W" or line.split()[1][0]=="X" or line.split()[1][0]=="Y" or line.split()[1][0]=="Z"):
            temp += line.split()[1][0] + "\""
        else:
            for i in range(1, len(line.split())-1):
                temp += line.split()[i] + " "
            temp += line.split()[-1]
            temp += "\""
    
    if(line == "------------------------------------------------------------------------------------------\n"):
        temp += "}"
        final += ", " + temp
        print(temp)
        temp = "{\"subject\":\"Biology\", "

