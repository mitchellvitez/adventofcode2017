import os

for i in range(1, 26):
    print(f"Program {i}")
    os.chdir(f"./day{str(i).zfill(2)}")
    if i < 5:
        os.system(f"time ./day{i}")
    else:
        os.system(f"time pypy3 day{i}.py")
    os.chdir("..")
    print("---")
    print()

