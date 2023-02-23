# 8. Write a program that validates name and age as entered by the user to determine whether
# the person can cast a vote or not using user defined exception

def setVotingAge():
    votingAge = int(input("Enter the age at which a person is eligible to vote: "))
    return votingAge

def isEligible(age):
    if age>=votingAge:
        return True
    else:
        return False

votingAge = setVotingAge()
ch =-1
while ch!=0:
    ch = int(input("\n0.Exit 1.Check eligibility of user 2.Set new voting age :\n"))

    if ch== 1:
        name = input("\nEnter your name: ")
        age = int(input("\nEnter your age: "))
        if isEligible(age):
            print(f"\n{name} is eligible to vote")
        else:
            print(f"\n{name} is not eligible to vote")

    if ch == 2:
        votingAge = setVotingAge()

