def reserve():
   for i in range(1,16):
       print(f"[ {i} ]", end = "  ")
       if i % 5 == 0:
           print("\n")

reserve()