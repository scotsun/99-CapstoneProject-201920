class DelegateLaptop(object):

    def __init__(self):
        pass

    def roboprint(self, message):
        if message == "1":
            print("A source of oil is detected")
        elif message == "2":
            print("A source of metal is detected")
        elif message == "3":
            print("Nothing found yet")
