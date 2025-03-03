#  2) მოცემული კოდი გადაიტანეთ Vscode-ში და გაასწორეთ შეცდომები, რათა სწორად იმუშაოს:

Status =  "Student"

if Status == "student":
   print(True)
else:
    print(False) 

# 3) კომენტარის სახით ახსენით თუ რომელ keyword-ებს ვიყენებთ conditional statement-ებში. ამასთანავე, დეტალურად ჩამოაყალიბეთ conditional statements-ის სინტაქსი

# Python-ში გამოყენებულია if, elif და else keyword-ები

# ჯერ უნა დავუწეროთ if keyword-ი რომლის შემდეგაც ვწერთ გარკვეულ პირობას. პირობის შემდეგ აუცილებელია ორი წერტილი და ინდენტაცია. elif და else keyword-ზე იგივე სინტაქს ვიყენებთ განსხვავება ისაა რომ ელსს არ ჭირდება პირობის გაწერა.

# 4) ცვლადში შეინახეთ თქვენი საყვარელი სიმღერის სახელი, შემდეგ კი მომხმარებელს შემოატანინეთ მისი საყვარელი სიმღერა. იმ შემთხვევაში თუ თქვენი და მომხმარებლის საყვარელი სიმღერა ემთხვევა - გამოიტანეთ "we have the same favorite song", სხვა შემთხვევაში კი გამოიტანეთ "we have different favorite songs"

song = "everything_from_skz"

song1 = (input("enter ur fav song: "))

if song == song1:
    print("we have the same favorite song")
else:
    print("we have different favorite songs ")

# 5) მოცემული Flowchart-ის მიხედვით დაწერეთ if else statement-ებისგან შემდგარი კოდი, და კომენტარის სახით დაწერეთ თუ რა იქნება კოდის შედეგი მაშინ, როდესაც მომხმარებელი არის სტუდენტი და მის მიერ შემოტანილი ასაკი იქნება 17

age = 17
status = "stuent"

if status == "stuent":
    if age < 18:
        print("too young student")
    else:
        print("ur adult student")
else:
    if age < 18:
        print(" too young not stuent")
    else:
        print("adult not student")

