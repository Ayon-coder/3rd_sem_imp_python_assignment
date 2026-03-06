max_cookie = 24
max_box = 75
cookie_input = int(input("Enter no of cookies: "))

needed_box = cookie_input // max_cookie
needed_container = needed_box // max_box

print("Number of boxes: ", needed_box)
print("Number of contaienr: ", needed_container)

if(cookie_input % max_cookie != 0):
    print("The leftover cookie is: ", cookie_input % max_cookie)
else:
    print("There is no leftover cookie")

if(needed_box % max_box != 0):
    print("The reamining boxes are: ", needed_box % max_box)
else:
    print("There is no leftover boxes")



    