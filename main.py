FILE = "notes.txt"

def add_note():
    note = input("Enter note: ")
    with open(FILE, "a") as f:
        f.write(note + "\n")

def show_notes():
    try:
        with open(FILE) as f:
            print(f.read())
    except:
        print("No notes yet")

while True:
    print("1.Add note")
    print("2.Show notes")
    print("3.Exit")

    choice = input("Choose: ")

    if choice == "1":
        add_note()
    elif choice == "2":
        show_notes()
    elif choice == "3":
        break
