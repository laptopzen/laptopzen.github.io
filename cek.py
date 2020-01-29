import os, re

minimal_kata = 300

postingan = os.listdir("_posts")

kata = []
for x in postingan:
    file = open(f"_posts/{x}", "r")
    data = file.read()
    regex = re.compile("\W+").split(data)
    regex = list(filter(None, regex))
    jumlah = len(regex)
    kata.append(jumlah)
    file.close()

nggak_lolos = []
kata_nggak_lolos = []
for n, x in enumerate(kata):
    if x < minimal_kata:
        nggak_lolos.append(postingan[n])
        kata_nggak_lolos.append(kata[n])

print(f"""Postingan yang kurang dari {minimal_kata} kata:
""")
for n, x in enumerate(nggak_lolos):
    print(f"- {x} ({kata_nggak_lolos[n]} kata)")