import random
#input voter details 
name = input("Please enter your name: ")
regNo = input("Please enter your matric number: ")
age = int(input("Please enter your age"))
schFee = input("Have you paid your school fee?\nType 'Yes' or 'No'")
schFee = schFee.lower()
ageDiff = 18 - age
eligYr = 2025 + ageDiff
year=int(regNo.split("/")[0])
ID = int(regNo.split("/")[1])
yrsInSch=2025-year
level = f"{yrsInSch}00 Level"
no = random.randint(1,10)
votingID = year + ID

#Messages
welcome = "Welcome to the NUESA Electoral Portal"
ageError = f"""The minimum age required for voting is 18.
You'd be able to vote in the {eligYr} election

"""
regError = f"""First years are not eligible to vote

"""
feeError = """Your school fees must be paid to be eligible to vote
"""
eligmsg = f"""Dear {name},
You are eligible to vote!!!
Wait while we generate a voting ID number for you:

Generating...
Generating...

Your voting ID is: 2025/{votingID}/{no}

Thanks for voting
"""
def messages ():
    if age < 18 and year > 2023 and schFee == "no":
        print(ageError + regError + feeError) 
    elif age < 18 and year > 2023:
        print(ageError + regError)
    elif age < 18 and schFee == "no":
        print(ageError + feeError)
    elif year > 2023 and schFee == "no":
        print(regError + feeError)
    elif year > 2023:
        print(regError)
    elif age < 18:
        print(ageError)
    else:
        print(eligmsg)
messages()
