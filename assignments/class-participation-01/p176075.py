import re


def check_for_email_validation(email):
    # email = raw_input("Enter your email : ")
    
    valid_domain_lst = ["gmail.com" , "hotmail.com", "live.com", "yahoo.com"]
    pattern = "[a-zA-Z]+[0-9]*[-.]*[a-zA-Z]+[0-9]*"
    email_lst = email.split("@")
    domain = email_lst[1]
    username = email_lst[0]
    if len(email_lst) == 2:
        if domain in valid_domain_lst:
            res = re.match(pattern, username)
            if(res.group(0) == username):
                return True
            else:
                return False
        else:
            # print("Invalid Email domain")
            return False
    else:
        print("Invalid use of this symbol @")
        return False






assert check_for_email_validation("AliAhmed@gmail.com") ==  True

assert check_for_email_validation("mehmoo---@gmail.com") ==  False

assert check_for_email_validation("Ahsan123_@gmail.com") ==  False

assert check_for_email_validation("Bashir_12@gmail.com") ==  False

assert check_for_email_validation("Bashir-a123@gmail.com") ==  True
