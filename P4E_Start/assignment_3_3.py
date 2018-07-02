try:
    score = input("Enter Score: ")
    s = float(score)
except:
    print("Not a valid score")
    quit()

if s > 1.0 or s < 0:
    print("Score is out of range")
elif s >= 0.9:
    print("A")
elif s >= 0.8:
    print("B")
elif s >= 0.7:
    print("C")
elif s >= 0.6:
    print("D")
else:
    print("F")
