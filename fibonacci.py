num=int(input('2이상의 숫자를 입력하시오: '))
arr=[0,1]

for i in range(2,num+1):
    n=arr[i-1]+arr[i-2]
    arr.append(n)
    i+=1

print(arr)