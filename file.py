from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

def ainstruction(list):
    i=0
    for x in list:
        if x[0]=='@':
            y=f'{(eval(x[1:-1])):016b}'
            list[i]=y+"\n"
        i=i+1;
    return list

def cinstruction(list):
    comp={  '0':'0101010',
            '1':'0111111',
            '-1':'0111010',
            'D':'0001100',
            'A':'0110000',
            'M':'1110000',
            '!D':'0001101',
            '!A':'0110001',
            '!M':'1110001',
            '-D':'0001111',
            '-A':'0110011',
            '-M':'1110011',
            'D+1':'0011111',
            '1+D':'0011111',
            'A+1':'0110111',
            'M+1':'1110111',
            '1+A':'0110111',
            '1+M':'1110111',
            'D-1':'0001110',
            'A-1':'0110010',
            'M-1':'1110010',
            'D+A':'0000010',
            'D+M':'1000010',
            'A+D':'0000010',
            'M+D':'1000010',
            'D-A':'0010011',
            'D-M':'1010011',
            'A-D':'0000111',
            'M-D':'1000111',
            'D&A':'0000000',
            'D&M':'1000000',
            'D|A':'0010101',
            'D|M':'1010101',
            'A&D':'0000000',
            'M&D':'1000000',
            'A|D':'0010101',
            'M|D':'1010101'}
    
    dest = {'':'000',
            'M':'001',
            'D':'010',
            'MD':'011',
            'DM':'011',
            'A':'100',
            'AM':'101',
            'MA':'101',
            'AD':'110',
            'DA':'110',
            'AMD':'111',
            'ADM':'111',
            'MAD':'111',
            'MDA':'111',
            'DMA':'111',
            'DAM':'111'}

    jump = {'':'000',
            'JGT':'001',
            'JEQ':'010',
            'JGE':'011',
            'JLT':'100',
            'JNE':'101',
            'JLE':'110',
            'JMP':'111'}
    
    i=0
    for x in list:
        y=''
        if x[0]!='@':
            x=x[0:-1]
            a=x.split("=")
            if(len(a)==1):
                b=a[0].split(";")
                desti=''
                if(len(b)==1):
                    comput=b[0]
                    jumps=''
                else:
                    comput=b[0]
                    jumps=b[1]
            else:
                desti=a[0]
                b=a[1].split(";")
                if(len(b)==1):
                    comput=b[0]
                    jumps=''
                else:
                    comput=b[0]
                    jumps=b[1]
            
            list[i]="111"+comp[comput]+dest[desti]+jump[jumps]+'\n'
        i=i+1

    return list


def labelling(list,symbol):
    u=0
    for x in list:
        if(x[0]=='('):
            symbol[x[1:-2]]=str(u)
        else:
            u=u+1
            continue;
    return symbol

def variabling(list,symbol):
    a=16;
    for x in list:
        if(x[0]=='@'):
            if x[1:-1] in symbol:
                continue;
            else:
                if x[1:-1].isdigit():
                    continue;
                else:
                    symbol[x[1:-1]]=str(a);
                    a=a+1;
    return symbol

def replacing(list,symbol):
    i=0
    for x in list:
        if x[0]=="@":
            if(x[1:-1] in symbol):
                x="@"+symbol[x[1:-1]]+"\n"
                list[i]=x
        i=i+1
    
    return list

def removing(list):
    i=0
    while(i<len(list)):
        x=list[i]
        if x[0]=="(":
            del list[i]
            i=i-1        
        i=i+1
    return list

def cleaning(code):
    code=[s.split("//")[0] for s in code]
    code=[s.replace("\n",'') for s in code]
    code=[s.replace(" ",'')for s in code]
    code=[x for x in code if x!='']
    code=[s+'\n' for s in code]

    return code


def functiontodo():
    name=filedialog.askopenfilename(initialdir = "/",title = "Select a File",filetypes = (("Text files",".txt"),("all files","*.*")))
    
    file1=open(name,'r')

    code = file1.readlines();

    file1.close();




    symbol = {'R0':'0',
            'R1':'1',
            'R2':'2',
            'R3':'3',
            'R4':'4',
            'R5':'5',
            'R6':'6',
            'R7':'7',
            'R8':'8',
            'R9':'9',
            'R10':'10',
            'R11':'11',
            'R12':'12',
            'R13':'13',
            'R14':'14',
            'R15':'15',
            'KBD':'24576',
            'SCREEN':'16384',
            'SP':'0',
            'LCL':'1',
            'ARG':'2',
            'THIS':'3',
            'THAT':'4'}



    name2=name.split(".")[0] + ".hack"
    file2=open(name2,'w')
    code=cleaning(code)
    symbol=labelling(code,symbol)
    symbol=variabling(code, symbol)
    code=replacing(code,symbol)
    code=removing(code)
    code=cinstruction(code)
    code=ainstruction(code)
    print(symbol)

    file2.writelines(code)
    messagebox.showinfo("showinfo", "The binary in written in"+name2)


functiontodo()