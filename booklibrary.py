import csv
from datetime import datetime, timedelta

# -------------------- Phase 1: Books --------------------

def load_catalogue(csv_filename):
    catalogue = []
    try:
        with open(csv_filename, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                row["Year Published"] = int(row["Year Published"])
                row["Number of Available Copies"] = int(row["Number of Available Copies"])
                catalogue.append(row)
    except FileNotFoundError:
        pass
    return catalogue


def save_catalogue(csv_filename, catalogue):
    with open(csv_filename, "w", newline="", encoding="utf-8") as f:
        fieldnames = ["Title", "Author", "Year Published", "ISBN", "Number of Available Copies"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for book in catalogue:
            writer.writerow(book)


def add_book(catalogue, title, author, year, isbn, copies):
    catalogue.append({
        "Title": title,
        "Author": author,
        "Year Published": int(year),
        "ISBN": isbn,
        "Number of Available Copies": int(copies)
    })


def display_books(books_list):
    if not books_list:
        print("No books found.")
        return
    print(f"{'Title':30} {'Author':20} {'Year':6} {'ISBN':20} {'Copies'}")
    for b in books_list:
        print(f"{b['Title'][:30]:30} {b['Author'][:20]:20} {b['Year Published']:6} {b['ISBN']:20} {b['Number of Available Copies']}")


def search_by_title(catalogue, keyword):
    return [b for b in catalogue if keyword.lower() in b["Title"].lower()]


def search_by_author(catalogue, author):
    return [b for b in catalogue if author.lower() in b["Author"].lower()]


def sort_by_title(catalogue):
    catalogue.sort(key=lambda b: b["Title"].lower())


def sort_by_year(catalogue):
    catalogue.sort(key=lambda b: b["Year Published"])


# -------------------- Phase 2: Users --------------------

def load_users(csv_filename):
    users = []
    try:
        with open(csv_filename, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                row["Outstanding Fines"] = float(row["Outstanding Fines"])
                row["Books Borrowed"] = eval(row["Books Borrowed"])
                users.append(row)
    except FileNotFoundError:
        pass
    return users


def save_users(csv_filename, users):
    with open(csv_filename, "w", newline="", encoding="utf-8") as f:
        fieldnames = ["User ID", "Full Name", "Email", "Address", "Books Borrowed", "Outstanding Fines"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for user in users:
            writer.writerow({
                "User ID": user["User ID"],
                "Full Name": user["Full Name"],
                "Email": user["Email"],
                "Address": user["Address"],
                "Books Borrowed": user["Books Borrowed"],
                "Outstanding Fines": user["Outstanding Fines"]
            })


def register_user(users, full_name, email, address):
    user_id = f"LIB{len(users)+1:04d}"
    new_user = {
        "User ID": user_id,
        "Full Name": full_name,
        "Email": email,
        "Address": address,
        "Books Borrowed": [],
        "Outstanding Fines": 0.0
    }
    users.append(new_user)
    return user_id


def display_user_details(users, user_id):
    for u in users:
        if u["User ID"] == user_id:
            print(u)
            return
    print("User not found.")


def pay_fine(users, user_id):
    for u in users:
        if u["User ID"] == user_id:
            u["Outstanding Fines"] = 0.0
            print("Fine cleared.")
            return
    print("User not found.")


# -------------------- Phase 3: Borrowing/Returning --------------------

def borrow_book(users, catalogue, user_id, book_title):
    user = next((u for u in users if u["User ID"] == user_id), None)
    if not user:
        print("User not found.")
        return
    if user["Outstanding Fines"] > 0:
        print("Clear fines before borrowing.")
        return
    book = next((b for b in catalogue if b["Title"].lower() == book_title.lower()), None)
    if not book:
        print("Book not found.")
        return
    if book["Number of Available Copies"] <= 0:
        print("No copies available.")
        return
    due_date = datetime.now() + timedelta(days=14)
    user["Books Borrowed"].append({"Title": book["Title"], "Due Date": due_date.strftime("%Y-%m-%d")})
    book["Number of Available Copies"] -= 1
    print(f"Book borrowed successfully. Due: {due_date.date()}")


def return_book(users, catalogue, user_id, book_title, return_date):
    user = next((u for u in users if u["User ID"] == user_id), None)
    if not user:
        print("User not found.")
        return
    borrowed = next((b for b in user["Books Borrowed"] if b["Title"].lower() == book_title.lower()), None)
    if not borrowed:
        print("This book was not borrowed.")
        return
    due_date = datetime.strptime(borrowed["Due Date"], "%Y-%m-%d")
    return_date = datetime.strptime(return_date, "%Y-%m-%d")
    days_late = (return_date - due_date).days
    if days_late > 0:
        fine = days_late * 2
        user["Outstanding Fines"] += fine
        print(f"Late return. Fine: ${fine}")
    # restore book copy
    book = next((b for b in catalogue if b["Title"].lower() == book_title.lower()), None)
    if book:
        book["Number of Available Copies"] += 1
    user["Books Borrowed"].remove(borrowed)
    print("Book returned successfully.")
