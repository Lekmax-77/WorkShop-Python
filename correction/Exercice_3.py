
def exerciceThree(max):
  i = 0
  while i < max:
    print(i)
    val = (yield i)
    # If value is sent, change counter
    if val is not None:
      i = val
    else:
      i += 1

# gen = exerciceThree(10)
# print(next(gen))
# print(next(gen))
# # send new value
# print(gen.send(6))
# print(next(gen))