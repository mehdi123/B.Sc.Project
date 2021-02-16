def reverseString(s):
    'just reverse the input string'
	rs=''
	for i in range(len(s)-1, -1, -1):
		rs += s[i]
	return rs

def addSymbolic(number1, number2):
    'addition of two large number given in the string format'
	index=0
	carry=0
	result=''
	num1=reverseString(number1)
	num2=reverseString(number2)
	minLength = min(len(num1), len(num2))
	while index<minLength:
		sum=int(num1[index])+int(num2[index])+carry
		result = str(sum%10) + result
		carry=sum/10
		index+=1
	single=''
	if len(num1)>len(num2):
		single=num1
	elif len(num1)<len(num2):
		single=num2
	while index < len(single):
		sum=int(single[index])+carry
		result = str(sum%10) + result
		carry = sum/10
		index += 1
	if carry != 0:
		result = str(carry)+result
	return result

if __name__=='__main__':
    print addSymbolic('1234567654321', '1234567256398659856') 