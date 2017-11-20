back = input("Type your message: ")
reverse = ""
count = len(back)
for letter in back:
    count -= 1
    reverse += back[count]

print(reverse)
