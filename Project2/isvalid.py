import re
from datetime import datetime

def isValidNumber(number):
    number = number.strip()
    if number.isdigit():
        return True
    else:
        return False    

def isValidCreditCardNumber(number):
    counter = 0
    for i in range(len(number)):
        if number[i].isdigit():
            counter += 1

    if counter != 16:
        return False   
            
    pattern = ('^[\d{4}]+[ .-_]+[\d{4}]+[ .-_]+[\d{4}]+[ .-_]+[\d{4}]$')

    if re.search(pattern, number) and len(number) in (16, 19):
        return True
    
    return False

def isValidUrl(url):
    
        if url[:11] != "http://www." and url[:12] != "https://www.":
            return False

        if url[-4] != "." and url[-3] != ".":
            return False

        if url[-3:].isalpha() or url[-2:].isalpha():
            return True
        return False    

def isValidDate(n):
    try:
        day, month, year = n.split(n[2])
    except:
        if not n[2].isalnum():
            n.replace(n[2], "/")
            day, month, year = n.split("/")
        else:
            return False

    valid = True

    try:
        datetime(int(year), int(month), int(day))
    except:
        valid = False

    if(valid):
        return True
    else:
        return False

def isValidMobilePhoneNumber(number):
    count = 0
    Armenian_phone_codes = ["93", "94", "98", "77", "95", "55", "43", "91", "96", "99"]
    pattern = "[a-z]|[A-Z]"

    if re.search(pattern, number):
        return False
         
    if number.startswith("0") and (len(number) in (9, 11, 12)):
        number = number.strip()
              
        for i in range(3, len(number)):
            if number[i].isdigit():
                count += 1

        if number[1:3] in Armenian_phone_codes and count == 6:
            return True
        else:
            return False

    elif number.startswith("+374") and len(number) in (12, 14, 15, 16):
        count = 0
        for i in range(4, len(number)):
            if number[i].isdigit():
                count += 1

        if number[4] not in [" ", "_", "-", "."]:
            if number[4:6] in Armenian_phone_codes and count == 8:
                return True
            else:
                return False
        else:
            if number[5:7] in Armenian_phone_codes and count == 8:
                return True
            else:
                return False

    return False                    

def isValidEmail(email):
    pattern = "^\w+[_.-]?\w+[@]+[a-z]+[.]\w{2,3}$"
    if re.search(pattern, email):
        return True
    else:
        return False
