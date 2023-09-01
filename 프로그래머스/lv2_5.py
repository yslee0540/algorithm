#파일명 정렬
answer = []
files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]

# for file in files:
#   number_check = False
#   head, num, tail = '', '', ''
#   for i in range(len(file)):
#     if file[i].isdigit():
#       num += file[i]
#       number_check = True
#     elif not number_check:
#       head += file[i]
#     else:
#       tail = file[i:]
#       break
#   answer.append((head, num, tail))

# answer.sort(key=lambda x: (x[0].upper(), int(x[1])))
# print([''.join(i) for i in answer])

#숫자 변환하기
def change_num(x, y, n):
  answer = 0
  s = set()
  s.add(x)

  while s:
    if y in s:
      return answer

    nxt = set()
    for i in s:
      if i+n <= y:
        nxt.add(i+n)
      if i*2 <= y:
        nxt.add(i*2)
      if i*3 <= y:
        nxt.add(i*3)
    s = nxt
    print(s)
    answer+=1

  return -1
print(change_num(10, 70, 5))
