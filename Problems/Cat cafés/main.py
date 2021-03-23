cafes = []
no_cats = []
while True:
    usr_input = input()
    if usr_input == "MEOW":
        break
    cafe, cat = usr_input.split()
    cafes.append(cafe)
    no_cats.append(int(cat))
max_element = max(no_cats)
idx_max = no_cats.index(max_element)
print(cafes[idx_max])
