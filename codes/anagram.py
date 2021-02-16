import SelectionSort as sorter

def readWords(sentinel='!'):
    words=[]
    word=''
    while word!=sentinel:
        word=raw_input()
        words.append(word)
    return words

def printItOut(signed):
    for group in signed:
        for item in group:
            print item,
        print
    
def listToStr(chars):
    'transform a list into a string'
    st=''
    for ch in chars:
        st+=ch
    return st

def sign(words, bound):
    signed={}
    for w in words:
	wl=w.lower()
        listed=list(wl)  # convert the string into list
        sorter.selectionSort(listed)  # or listed.sort(), builtin list type sort function
        sorted=listToStr(listed)
        found=signed.get(sorted, [])
        found.append(w)
        signed[sorted]=found
    return [signed[key] for key in signed if len(signed[key]) > bound]

if __name__=='__main__':
    signed=sign(readWords(), 4)
    printItOut(signed)
