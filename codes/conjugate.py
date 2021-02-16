def rotate(str, direction):
    'rotates the string one step. the direction specifies the left or right rotation'
    if direction==1:    #right
        return str[-1]+str[:-1]
    else:
        return str[1:]+str[0]
    
def isConjugate(str1,str2):
    'check if two input string are conjugates or  not'
    if len(str1) != len(str2):
        return 0
    for i in range(len(str1)):
        if str1==str2:
            return 1
        str1=rotate(str1,1)
    return 0

if __name__=='__main__':
    print isConjugate('aabbcc', 'aabbccd')