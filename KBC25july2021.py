question_list =[

    "how many continents are there?",
    "what is the capital of india?",
    "NG mai kon se course padhaya jata hai?",
]
option_list=[
    ["four","nine","seven","eight"],
    ["chandigarh","bhopal","chennai","dehli"],
    ["softwere engineering","counseling","tourism","agriculture"]
]


solution_list=[3,4,1]
answer_list=[
    ["1.four","3.seven"],
    ["2.bhopal","4.delhi"],
    ["1.softwere engineering","4.Agriculture"]

]
print("kaun banega cororepati (kbc)")
i=0
s=0
count=0
while i<len(question_list):
    print(question_list[i])
    j=0
    k=1
    while j<len(option_list[i]):
        print(k,".", option_list[i][j])
        k+=1
        j+=1
    num1=input("do u want 50 50 lifeline")
    if num1=="yes":
        print("50 50 lifelin")
        if count<1:
            print(answer_list[i])
            num2=int(input("enter the answer"))
            if num2==solution_list[i]:
                s=+10000
                print("your answer is correct")
                print("u win Rs/",s)
            else:
                print("ur answer is incorrect")
                break
            count+=1
            
        else:
            print("u already use life line")
            m=int(input("enter ur answer"))
            if m==solution_list[i]:
                print("congrats, ur answer is right")
                s=s+10000
                print("u win",s)
            else:
                print("ur answer is wrong")
                print("u can play again")
                print("u win",s)
                break
    else:
        k=int(input("enter your answer"))
        if k==solution_list[i]:
            print("right answer")
            s+=100000
            print("u win Rss/",s)
            print("congrss")
        else:
            print("no chance")
            print("ur answer is wrong")
            break
    i=i+1