import sys
if len(sys.argv) >= 4:
    principle = float(sys.argv[1])
    time = float(sys.argv[2])
    rate = float(sys.argv[3])
    print("User input provided.")
else:
    principle = 1000
    time = 2
    rate = 2
si = (principle* time * rate) / 100
print("The Principal is :", principle)
print("The Time is :", time)
print("The Rate is :", rate)
print("The Simple Interest is :", si)
