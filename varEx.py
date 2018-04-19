import operator
import requests
import cred

# ar cia taip reikejo?
def draw_grid(param1, x, y):
    my_list = []
    for i in range(0, param1):
        hor_list = []
        for n in range(0, param1):
            hor_list.append("_")
        my_list.append(hor_list)
    my_list[x][y] = "X"
    #print(my_list)

    return my_list

#gal kazkaip protingiau?
my_grid = draw_grid(4, 0, 0)
x_pos = 0
y_pos = 0

print(my_grid)

# Move X per grid
def move_x(my_grid):
    #global my_grid
    x_pos = y_pos = 0
    for i in range(0, len(my_grid)):
        for n in range(0, len(my_grid[i])):
            my_grid[x_pos][y_pos] = "_"
            my_grid[i][n] = "X"
            x_pos = i
            y_pos = n
            for z in my_grid:
                print(z)
            print()

move_x(my_grid)

def turn_sentence(text):
    print("orginalus tekstas: " + text)
    split_text = " ".join(list(reversed(text.split(" "))))
    print(split_text)
    print(split_text[::-1])

turn_sentence("labas rytas kaip tau sekas")

def matematika(*argv):
    actions = (operator.add, operator.mul, operator.sub)
    sum = 0
    iter = -1
    for i in argv:
        if iter == -1:
            sum = i
            iter = 0
            continue
        elif iter > 2:
            iter = 0
        try:
            sum = actions[iter](sum, i)
            iter += 1
        except Exception:
            print("Klaida")
            break
    print(sum)

matematika(20, 1, 2, 2)

#
# 2 Paskaita
#

line = "It's so cool to learn {}! "

with open("values.txt", "r") as rf:
    names = rf.read()
    words = names.split(",")
    rf.close()

#for word in words:
new_line = ((line.format(" ".join(words)) * 2) + "\n")*2

with open("linija.txt", "w+") as f:
    f.write(new_line)
    f.seek(0,0)
    print(f.read())
    f.close()


with open("hw.txt", "w+") as fh:
    names = ('to fly', 'Python', 'Java')
    for name in names:
        fh.write(((("It's so cool to learn {}!".format(name) + ' ') * 2)+'\n')*11)
    fh.seek(0,0)
    print(fh.read())
    fh.close()

req = requests.get("https://api.github.com/user", auth=("virtualas10", cred.login["password"]))
with open("req.txt", "w+") as rfile:
    rfile.write(req.text)
#    rfile.write(req.json())

print(req.status_code)
print(req.text)
print(req.json())
