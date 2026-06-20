#problem to solve the nums of digits plus one
def plusone(digits):
    carry=1
    for i in range(len(digits)-1,-1,-1):
        sum=digits[i]+carry
        digits[i]=sum%10
        carry=sum//10
    if carry==1:
        digits.insert(0,1)
    return digits
digits=[1,2,3,4]
print(plusone(digits))




