def show_version():
    with open("version.txt","r") as f:
        print("Library Management System",f.read())

def show_books():
    with open("books.txt","r") as f:
        print("\nAvailable Books:")
        print(f.read())

show_version()
show_books()
