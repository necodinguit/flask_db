

class Hey(metaclass=type):
    def __init__(self, arg):
        self.arg = arg

    def main(self):
        print("!!!!!!!!!!!!!!!!!!!!!")



AAA =  meta("Class", (object,), {"__init__": __init__})

if __name__ == "__main__":
    Hey("asdfasdf").main()
    AAA("aaa").main()