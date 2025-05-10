class chatbook:
    def __init__(self):
        self.username = ""
        self.pwd = ''
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
            self.signup()
         elif user_input == "2":
            self.signin()
         elif user_input == "3":
             self.my_post()
         elif user_input == "4":
             self.sendmsg()
         else:
             exit()




    def signup(self):
        email = input('Enter your email here -- >')
        password = input('setup your password here -- >')
        self.username = email
        self.password= password
        print('you have signed up successfully ')
        print("\n")
        self.menu()


    def signin(self):

        if self.username == " " and self.password=="":
            print("Please signup first by pressing 1 in the main menu")
        else:
            uname = input('Enter your email here -- >')
            pwd = input('setup your password here -- >')
            if self.username==uname and self.password==pwd:
                print("you have signed in successfully !!")
                self.logging=True
            else:
                print("Please input correct credential..")  

        print("\n")
        self.menu()          

    def my_post(self):
        if self.logging == True:
            text = input("Enter your meassage here --> ")
            print(f"following contend has been posted {text}")
        else:
            print('you need to signin first to post something') 
        print("\n")
        self.menu()       


    def sendmsg(self):
        if self.logging==True:
            text=input("Enter your message here - > ")
            frnd = input("whom to send the msg - >")
            print(f"your message has been sent to {frnd}")
        else:
            print('you need to signin first to post something') 
        print("\n")
        self.menu()      



odj = chatbook()
