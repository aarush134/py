def no_notes(a):
    Q = [2000, 500, 200, 100, 50, 20, 10]
    
    for q in Q:
        x = a // q 
        print("Notes of {} = {}".format(q, x))
        a = a % q  


amount = int(input("Enter Total Amount: "))
no_notes(amount)
