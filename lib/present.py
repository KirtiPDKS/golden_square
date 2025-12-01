class Present:
    def __init__(self):
        self.contents = None

    def wrap(self,contents):
        #print(self.contents)
        if self.contents is not None:
            raise Exception ("Contents has already been wrapped.")
        self.contents = contents

    def unwrap(self):
        if self.contents is None:
            raise Exception("No contents have been wrapped.")
        return self.contents


# present1 = Present()
# x = present1.wrap("ball")
# print(f"function1: {x}")
# print (f"One: {present1.contents}")
# present1.unwrap()
# print (f"Two: {present1.contents}")