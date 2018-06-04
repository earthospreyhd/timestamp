import timestamp
import datetime

while True:
    choice = input("Enter \"sign\" to sign a hash or \"verify\" to verify: ")


    if (choice == "sign"):
        messhash = input("Enter your message or hash: ")
        sigfile = input("Where would you like to save your signature?: ")
        url = "http://localhost:8000/sign/"
        signature = timestamp.signTime(messhash, url)
        sigfile = open(sigfile, "w")
        sigfile.write(signature)
        sigfile.close()
        print("Your message has been signed with the date ", datetime.date.today())
        break

    elif (choice == "verify"):
        messhash = input("Enter your message or hash: ")
        messhash = messhash.encode()
        sigfile = input("Enter the signature file name: ")
        date = input("Enter the date in the format YYYY-MM-DD: ")
        sigfile = open(sigfile, "r")
        signature = sigfile.read()
        sigfile.close()
        isvalid = timestamp.verifyTime(messhash, signature, date)
        if isvalid == True:
            print("The signature is correct!")
        else:
            print("The signature or time is incorrect")
        break
    else:
        print("Put in a valid option: ")