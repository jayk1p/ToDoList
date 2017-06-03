todo = []
# The todo list has to be global, and not within the "while" function
# b/c if it's in the while function, it will make the todo list
# equal to a blank list [] every time it loops

while True:

    raw = raw_input(" ")

    if raw:
        todo.append(raw)
        print todo


    if raw == "finished":
        print "finished"
        break
