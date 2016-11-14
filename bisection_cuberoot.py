number = input('Enter the number : ' )
number =  float(number)
change = 0.00001
low =0.0
high = max(1.0,number)
mid = (low+high)/2.0
while (abs(mid**3-number)>=change):
    if mid**3<number:
        low = mid
    else:
        high = mid
    mid =(low+high)/2.0
print 'The cube root of ', number ,' is ', mid
