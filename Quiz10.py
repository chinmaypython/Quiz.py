print("Welcome to the quiz! Enter yes to start and no to exit.")
start = input("--> ")
Right_answer = 0
Wrong_answer = 0
Total_answer = 0
if start.lower() == "yes":
    print("""1. What is the powerhouse of the cell?
    a.Mitochondria     b.Chloroplast
    c.Nucleus          d.None of these""")
    Ans = input("--> ")
    if Ans == "a" or Ans.lower() == "mitochondria":
        print("Right Answer!")
        Total_answer += 1
        Right_answer += 1
    else:
        print("Wrong Answer!")
        Total_answer += 1
        Wrong_answer += 1

    print("\n Total Questions --> ", Total_answer,
      "\n Right Answer --> ", Right_answer, 
      "\n Wrong Answer --> ", Wrong_answer)
   
    print("""2. Which of the following is a conductor:-
    a.Air              b.Glass  
    c.Metals           d.Rubber""")
    Ans = input("--> ")
    if Ans == "c" or Ans.lower() == "metals":
        print("Right Answer!")
        Total_answer += 1
        Right_answer += 1
    else:
        print("Wrong Answer!")
        Total_answer += 1
        Wrong_answer += 1

    print("\n Total Questions --> ", Total_answer,
      "\n Right Answer --> ", Right_answer, 
      "\n Wrong Answer --> ", Wrong_answer)
   
   
    print("""3. Which syntax is use to define an object in python?
    a.print            b.def        
    c.or               d.None of these""")
    Ans = input("--> ")
    if Ans == "b" or Ans.lower() == "def":
        print("Right Answer!")
        Total_answer += 1
        Right_answer += 1
    else:
        print("Wrong Answer!")
        Total_answer += 1
        Wrong_answer += 1

    print("\n Total Questions --> ", Total_answer,
      "\n Right Answer --> ", Right_answer, 
      "\n Wrong Answer --> ", Wrong_answer)
   
    print("""4. What is the capital of Germany?
    a.Berlin           b.Hamburg
    c.Austria          d.None of these""")
    Ans = input("--> ")
    if Ans == "a" or Ans.lower() == "berlin":
        print("Right Answer!")
        Total_answer += 1
        Right_answer += 1
    else:
        print("Wrong Answer!")
        Total_answer += 1
        Wrong_answer += 1

    print("\n Total Questions --> ", Total_answer,
      "\n Right Answer --> ", Right_answer, 
      "\n Wrong Answer --> ", Wrong_answer)   


    print("""5. What is the smallest country in the world?
    a.Bangladesh       b.Vatican city
    c.Sri Lanka        d.None of these""")
    Ans = input("--> ")
    if Ans == "b" or Ans.lower() == "vatican city":
        print("Right Answer!")
        Total_answer += 1
        Right_answer += 1
    else:
        print("Wrong Answer!")
        Total_answer += 1
        Wrong_answer += 1

    print("\n Total Questions --> ", Total_answer,
      "\n Right Answer --> ", Right_answer, 
      "\n Wrong Answer --> ", Wrong_answer)
      
                        
    print("""6. What is the biggest country in the world?
    a.USA              b.Russia 
    c.Canada           d.None of these""")
    Ans = input("--> ")
    if Ans == "b" or Ans.lower() == "russia":
        print("Right Answer!")
        Total_answer += 1
        Right_answer += 1
    else:
        print("Wrong Answer!")
        Total_answer += 1
        Wrong_answer += 1


    # Continue with the remaining questions...

    if Right_answer > 7:
        print("Congrats you passed the test and got", Right_answer, "right answers and", Wrong_answer, "wrong answers.")
    elif Right_answer < 7 and Right_answer > 5:
        print("You passed the test and got", Right_answer, "right answers and", Wrong_answer, "wrong answers. But you could try better next time")
    else:
        print("You failed the quiz and got", Right_answer, "right answers and", Wrong_answer, "wrong answers. Better luck next time.")
else:
    None
