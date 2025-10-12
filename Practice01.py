print("PthonVSCode_101225 >> Code101225 >> Practice01.py >> Welcome !! ")



def my_function01():
    print("hello >> my_function01!!")
    a = 2
    if a > 5:
        print("a is greater than 5")
    else:
        print("a is not greater than 5")
    match a:
        case 1: print("monday")
        case 2: print("tuesday")


def my_bigTicket():
    ticketPrize = 1000.00
    members = ["karthikeyanJayabalan", "arbindChristy", "karthikeyanRamalingam", "jay", "antonyPradeep", "subhashChand", "janitySoyza", 
               "mohan", "sasi", "harris", "mustafa", "robin", "ramesh"]
    members.sort()
    print("Total members:", len(members))
    for member in members:
        print(member.upper())
    eachPeronsShare = ticketPrize/len(members)
    print(f"Each person's share is {eachPeronsShare:.2f}")

def my_bigTicket01():
    ticketPrize = 1000
    members = ["karthikeyanJayabalan", "arbindChristy", "karthikeyanRamalingam", "jay", "antonyPradeep", "subhashChand", "janitySoyza", 
               "mohan", "sasi", "harris", "mustafa", "robin", "ramesh"]
    members.sort()
    print("")
    print("Total BigTicket Members:", len(members))
    print("+++++++++++++++++++++++++++")
    for index, member in enumerate(members):
        print(index+1, member.upper())
    eachPeronsShare = ticketPrize/len(members)
    print("")
    print("BigTicket cost:", ticketPrize)
    print("++++++++++++++++++++")

    print("")
    print(f"Each person's share is {eachPeronsShare:.2f}")
    print("++++++++++++++++++++++++++++")
    print("")

my_bigTicket01()



