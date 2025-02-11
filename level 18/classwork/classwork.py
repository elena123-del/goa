# 1)გამოიტანეთ რიცხვები 0-დან 10-ის ჩათვლით
for i in range(11):
    print(i)

# 2)გამოიტანეთ რიცხვები 50-დან 150-მდე
for i in range(50,150):
    print(i)

# 3)გამოიტანეთ მხოლოდ ლუწი რიცხვები 200-დან 500-მდე
for i in range(200,500,2):
    print(i)

# 4)გამოიტანეთ კენტი რიცხვები 0-დან 50-მდე
for i in range(50):
    print(i)

# 5)მომხმარებელს შემოატანინეთ ორი რიცხვი start,end,step და range ფუნქციის გამოყენებით გამოიტანეთ start იდან end ის ჩათვლით გამოიტანეთ ყველა რიცხვი
start = int(input("enter start num: "))
end = int(input("enter end num: "))
step = int(input("enter range num: "))



for i in range(start,end,step):
    print(i)


# 6) მომხმარებელს შემოატანინეთ სახელი და for ციკლის საშიალებით გამოიტანეთ ამ სახელის თითოეული ასო
name = input("enter ur name: ")

for letter in name:
    print(letter)
