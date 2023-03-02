# This is the Introduction of the Code SplitWise
a = 0  # To let the algorithm introduce itself only once!
if a == 0:
    print(
        "Hello Sir,\nI am your Personalized Splitwise Algorithm here to help you to maintain the record of your "
        "expenditure")
    my_name = input("\nMay I know your name please")
    print(f"Hi {my_name}")
    print("I think you are new to the application\nIts time to create your group\nWhat do you like to name your group")
    group = input()
    group_name = [group]
    a = 1
else :
    print(f"Hi {my_name}")