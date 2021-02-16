import string

def isDigit(char):
    'check whether the char is a digit or not'
    return char in string.digits
        
def decompressString(compstr):
    'decompresses a string. example: asd5e3f4g1 becomes asdddddeeeffffg'
    index=0
    result=''
    num=''
    previous=''
    while index<len(compstr):
        while index < len(compstr) and isDigit(compstr[index]):
            num += compstr[index]
            index+=1
        if len(num)>0:
            result += previous*(int(num)-1) # a copy of previous character is already concatenated
            num=''
            index -= 1
        else:
            result += compstr[index]
        previous=compstr[index]
        index+=1
    return result

if __name__=='__main__':
    print decompressString('d5e3f4g1')