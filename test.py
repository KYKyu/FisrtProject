print("hello")

def hello10():
    for _ in range(10):
        print("hello", end=" ")

hello10()
print("")
for i in range(1, 11):
    print("*", end="")
    if i % 5 == 0:
        print("")
