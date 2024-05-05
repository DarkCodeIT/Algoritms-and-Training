from collections import Counter
# def main():
#     n = int(input())
#     m = int(input())
#     k = int(input())
#     l = int(input())
#     s = int(input())

#     kg = k*m*n
#     if kg % l == 0:
#         ndd = int(kg/l)
#     else:
#         ndd = int(kg/l)+1
#     print(ndd*s)
# main()


    
# def main():
#     n = int(input())
#     m = int(input())
#     del_ploc = 2*n    
#     if n == 0:
#         return m+1
#     elif m == 0:
#         return del_ploc
    
#     retu

#     k = int(input())
 
#     s = '6'*n
#     print(s)
#     s = int(s)**2
#     print(s)
#     s = str(s)
#     print(s)
#     print(int(s[k-1]))
 
# main()

# def main():
#     w = int(input())
#     close = False
#     for i in range(2,w,2):
#         if close:
#             break
#         for j in range(2,w,2):
#             if i + j == w:
#                 print('YES')
#                 close = True
#                 break
#     if not close:
#         print('No')

# main()

# def main():
#     n = int(input())
#     data = ['']*n
#     for i in range(n):
#         word = input()
#         data[i] = word
    
#     for word in data:

#         if len(word) > 10:
#             ln = len(word[1:-1])
#             if ln == 0:
#                 print(f'{word[0]}{word[-1]}')

#             else:
#                 print(f'{word[0]}{ln}{word[-1]}')

#         else:
#             print(word)

# main()

# def main():
#     n = int(input())
#     k = 0
#     for i in range(n):
#         lst = list(map(int, input().split()))
#         ln = Counter(lst)
#         if ln[1] >= 2:
#             k += 1
#     print(k)

# main()



# def main():
#     nk = list(map(int, input().split()))
#     num = list(map(int, input().split()))
#     stp = Counter(num)
#     count = 0
#     for key in stp.keys():
#         if key >= num[nk[1]-1] and key != 0:
#             count += stp[key]
#     print(count)

# main()

# def main():
#     n = int(input())
#     x = 0
#     for i in range(n):
#         code = input()
#         if '-' in code:
#             x -= 1
#         else:
#             x += 1
#     print(x)

# main()

# def main():
#     mn = list(map(int, input().split()))
#     S = mn[0] * mn[1]   
#     print(S // 2)

# main()


# def main():
#     count = 0
#     for i in range(1,6):
#         n = input().replace(' ','')
#         if '1' in n:
#             count = abs(3 - i) + abs(3 - (n.index('1') + 1))
#             break
#         else:
#             continue

#     print(count)

# main()

# def main():
#     str1 = input().lower()
#     str2 = input().lower()
#     cou = 0
#     for i in range(len(str1)):
#         if str1[i] > str2[i]:
#             cou += 1
#             break
#         elif str1[i] < str2[i]:
#             cou -= 1
#             break

#     print(cou)

# main()

# def main():
#     s = list(map(int, input().split('+')))
#     s.sort()
#     print(*s, sep="+")
# main()

def main():
    s = input()
    print(s[0].upper() + s[1:])

main()