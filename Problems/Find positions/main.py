number_seq = list(input().split())
x = input()
if number_seq.count(x) == 0:
    print("not found")
else:
    indices = [str(index) for index, numb in enumerate(number_seq) if numb == x]
    print(" ".join(indices))
