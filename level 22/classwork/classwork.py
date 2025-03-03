# 1) კომენტარის სახით დაწერეთ, elif statement-ის სრული ფურმა და ახსენით თუ რა შემთხვევაში ვიყენებთ მას.

# elif = else if 
# if- თუ, მაგალითად თ 18 > 18 და რაღაც ეგრე
# else-სხვა , სხვა შემთხვევაში ვწერთ ამას

# 2) დაწერეთ ისეთი პირობა, რომლისთვისაც მხოლოდ if statement-ია საჭირო.

age = 17

if age > 18:
    print("ur adult")

# 3) ცვლადში შეინახეთ თქვენი საყვარელი ფილმის სახელი, შემდეგ კი მომხმარებელს შემოატანინეთ მისი საყვარელი ფილმი. იმ შემთხვევაში თუ თქვენი და მომხმარებლის საყვარელი ფილმები ემთხვევა - გამოიტანეთ "our movie taste is similar", სხვა შემთხვევაში კი გამოიტანეთ "we like different movies"

movie = "maze_runner"

movie2 = int(input("enter ur fav movie: "))

if movie == movie2:
    print("our movie taste is similar")
elif movie != movie2:
    print("we like different movies")