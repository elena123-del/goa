# 4)მომხმარებელს შემოატანინეთ რიცხვი და შეამოწმეთ, თუ რიცხვი მეტია 90-ზე, დაბეჭდეთ "A", თუ რიცხვი ნაკლებია 90-ზე და მეტია 70-ზე, დაბეჭდეთ "B", თუ რიცხვი ნაკლებია 70-ზე და მეტია 50-ზე, დაბეჭდეთ "C", სხვა შემთხვევაში დაბეჭდეთ "D"
score = int(input("Enter your number: "))

if score >= 90:
    print("A")
elif score < 90 and score > 70:
    print("B")
elif score < 70 and score > 50:
    print("C")
else:
    print("D")