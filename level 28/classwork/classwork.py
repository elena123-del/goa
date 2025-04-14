# <!-- 1)კომენტარის სახით ახსენით რას აკეთებს upper / lower / capitalize / find მეთოდები

# <!-- upper adidebs asoebs lower ki apataravebs. find edzebs imasos romelsac mivutitebt -->

# <!-- 2)მომხმარებელს შემოატანინეთ მისი სახელი და შეამოწმეთ, თუ მისის ასო იწყება დიდი ასოთი, მაშინ დაბეჭდეთ "Hello!", სხვა შემთხვევაში "Bye..." -->

name = input("Enter your name: ")

if name[0].isupper():
    print("Hello!")
else:
    print("Bye...")


# <!--3)მომხმარებელს შემოატანინე მისი გვარი, თუ ეს გვარი იწყება "m" ასოთი მაშინ დაბეჭდეთ მომხმარებლის შემოტანილი გვარი გადიდებული, თუ იწყება "g" ასოთი, მაშინ დაბეჭდეთ მომხმარებლის სახელი დაპატარავებული

name = input("Enter your name: ")
surname = input("Enter your surname: ")

if surname[0].lower() == 'm':
    print(surname.upper())
elif surname[0].lower() == 'g':
    print(name.lower())
else:
    print("Nothing to show.")

# 4)მომხმარებელს შემოატანინეთ მისი საყვარელი ფერი, თუ ეს ფერი შეიცავს "p" ასოს, მაშინ დაბეჭდეთ "Gamarjoba", სხვა შემთხვევაში "Naxvamdis" -->


favorite_color = input("შეიყვანეთ თქვენი საყვარელი ფერი: ")

if "p" in favorite_color.lower():
    print("Gamarjoba")
else:
    print("Naxvamdis")
