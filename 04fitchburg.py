"""
a1 = [1]
a2 = [1, 1]
a3 = [1,2,1]
a4 = [1,3,3,1]
a5 = [1,4,6,4,1]
median of a28
https://baijiahao.baidu.com/s?id=1611993057196886679&wfr=spider&for=pc
20058300 is triangle
"""

def pascal_triangle(n):
    if n < 2:
        return [1]
    line = [1,1]
    if n == 2:
        return line
    for i in range(2,n):
        temp = []
        for j in range(i-1):
            temp.append(line[j] + line[j+1])
        line = [1] + temp + [1]
    # print(line)
    return line

def medianOfAn(n):
    pt = pascal_triangle(n)
    idx = n // 2 + (1 if n % 2 > 0 else 0)
    return pt[idx]


print(medianOfAn(28))