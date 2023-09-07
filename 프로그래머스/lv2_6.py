#멀쩡한 사각형
import math
def find_square(w,h):
  return w * h - (w + h - math.gcd(w, h))

print(find_square(8, 12))

#하노이탑
def get_hanoi(n):
  answer = []
  def hanoi(n, start, end, sub):
    if n == 1:
      answer.append([start, end])
      return
    else:
      hanoi(n - 1, start, sub, end)
      #가장 큰 원반
      answer.append([start, end])
      hanoi(n - 1, sub, end, start)
  hanoi(n, 1, 3, 2)        
  return answer

print(get_hanoi(3))