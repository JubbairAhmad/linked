n = int(input())
x = True
bin = ''
while x:
    if n > 0:
        bin = str(n % 2) + bin
    else:
        x = False
    n = n // 2 
print(bin)
