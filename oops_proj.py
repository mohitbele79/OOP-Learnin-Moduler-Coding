class chatbook:
    def __init__(self):
        self.username = ""
        self.password = ''
        self.logging = False
        self.menu()


    def menu(self):
         user_input= input("""Welcome to chatbook !! How would you like to proceed ? 
                            1  Press 1 to Signup 
                            2. Press 2 to signin 
                            3. Press 3 to write an post
                            4. Press 4 to message a friend 
                            5. press any other key to Exit""") 
         if user_input =="1":
            pass
         elif user_input == "2":
            pass
         elif user_input == "3":
             pass
         elif user_input == "4":
            pass
         else:
             exit()



         
odj = chatbook()