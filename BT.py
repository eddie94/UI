class BT():

    def __init__(self):
        self.state = "Running"

    def sequence(self,node_list):

        self.state = "Running"

        for node in node_list:
            if type(node) == bool:
                if node == False:
                    self.state = "Failure"
                    return False
            else:
                PF = node()
                if PF == False:
                    self.state = "Failure"
                    return False

        self.state = "Success"
        return True

    def fallback(self,node_list):

        self.state = "Running"

        for node in node_list:
            if type(node) == bool:
                if node == True:
                    self.state = "Success"
                    return True
            else:
                PF = node()
                if PF == True:
                    self.state = "Success"
                    return True

        self.state = "Failure"
        return False

    def condition(self,action):

        PF = action()
        return PF

    def action(self):
        pass

    def parallel(self):
        pass

def move():
    print("move")

def walk():
    print("walk")

def check(num):
    if num > 0:
        print("big")
        return True
    else:
        print("small")
        return False

bt = BT()

a_list = [move,walk]
a = bt.sequence(a_list)
c = check(-1)
b_list = [c,a,move]
b = bt.fallback(b_list)