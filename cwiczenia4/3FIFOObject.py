class Fifoqueue:
    def __init__(self):
        self.queue = []

    def length(self):
        return len(self.queue)

    def show(self):
        for name in self.queue:
            print("waiting customer: {}".format(name))

    def add(self, name):
        self.queue.insert(0, name)

    def next(self):
        return self.queue.pop()


q1 = Fifoqueue()
q2 = Fifoqueue()
q1.add('Spearing')
q1.add('Fangohr')
q1.add('Takeda')
q2.add('John')
q2.add('Peter')
print("{} customers in queue1:".format(q1.length()))
q1.show()
q1.next()
print("{} customers in queue2:".format(q2.length()))
q2.show()
q2.next()
print("\n")
print("{} customers in queue1:".format(q1.length()))
q1.show()
print("{} customers in queue2:".format(q2.length()))
q2.show()