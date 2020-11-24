a1 = input() or 0
move = input()
a2 = input() or 0
result = None

if a1.isdigit() and a2.isdigit():
  a1, a2 = float(a1), float(a2)

  if move == '+':
    result = a1 + a2
  if move == '-':
    result = a1 - a2
  if move == '*':
    result = a1 * a2
  if move == '/':
    result = a1 / a2
  if move == '//':
    result = a1 // a2
  if move == '**':
    if a1 == '':
      result = a2 ** 0.5 
    else:
      result = a1 ** a2
  if move == '%':
    result = (a1 / 100) * a2
  if round(result, 2) == 3.14:
    print("ПИ")
  else:  
    print(result) 
