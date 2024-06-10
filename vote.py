a = 'voter.txt'
b = 'candidate.txt'

class vote ():
    def __init__(self):
        self.name = ""
        self.phone = ""
        self.vote = ""

    def get_details(self):
        self.name = str(input('what is your?\n1.name: '))
        self.phone = (input('2.phone no: '))
        with open(a,'a') as q:
            q.write(f"{self.name}--{self.phone}\n")

    def get_vote(self, vote):
        with open(b,'a') as w:
            w.write(f"\n{self.name} picks {vote}")

    def announce(self):
        with open(b) as x:
            x.readlines()

def candidates():
    print ('''
    ----------------------------candidates-------------------------------
    
        please pick a candidate u would like to lead u..select wisely !!!
                    1.austin
                    2.masharia
                    3.sandra
                    4.terry
                    5.jess
                    0.exit
                    
    ---------------------------------------------------------------------- ''')

def voting():
    voter = vote()
    voter.get_details()
    candidates()
    while True:
        user_vote = int(input('pick : \n'))
        if user_vote == 1:
            voter.get_vote("austin")
            break
        
        elif user_vote == 2:
            voter.get_vote("masharia")
            break

        elif user_vote == 3:
            voter.get_vote("sandra")
            break

        elif user_vote == 4:
            voter.get_vote("terry")
            break

        elif user_vote == 5:
            voter.get_vote("jess")
            break

        elif user_vote == 0:
            print(f"thank you for your vote :)")
            break

        else:
            print("value entered is not a digit between 0 to 5")
            candidates()

voting()