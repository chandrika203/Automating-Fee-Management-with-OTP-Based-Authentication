import Fee_Pending
import Fees_Paid
import otp

admin_username = input("Enter User Name: ")
if admin_username == "admin":
    otp = otp.send_otp("chandrikachavva5@gmail.com")
    y = int(input("Enter OTP: "))
    if y == otp:
        print("login success")
    else:
        print("Login Failed")
        exit()
else:
    print("Invalid Username")
    exit()

userdetails ={
    112 : ["Amyra","chandrikachavva5@gmail.com","false"],
    101 : ["Chandu","chandrikachavva23@gmail.com","false"],
    132 : ["Chandrika","chavvachandrika@gmail.com","true"]
    }

while True:
    print("Welcome Admin")
    print("Choose your option")
    print("1. EDit information")
    print("2. Send mail to fee pending users")
    print("3. send mail to no fees pending users")
    print("4. Exit")
    x = int(input("Enter Option: "))
    if x == 1:
        for user in userdetails:
            if userdetails[user][2] == "False":
                status = input(f"Enter the status of {userdetails[user][0]}: ")
                userdetails[user][2] = status.lower()
                print(f"{user[0]} data updated!")
        else:
            print("Data Edited")
    elif x == 2:
        res=[]
        for user in userdetails:
            if userdetails[user][2] == "false":
                res.append([userdetails[user][0],userdetails[user][1]])
        Fees_Paid.send_mails(res)
        print("Mails sent users to have clear fees")
    elif x == 3:
        res=[]
        for user in userdetails:
            if userdetails[user][2] == "true":
                res.append([userdetails[user][0],userdetails[user][1]])
        Fee_Pending.send_mails(res)
        print("Mails sent to all cleared users")
    else:
        print("Thank You")
        print("Visit again")
        break
