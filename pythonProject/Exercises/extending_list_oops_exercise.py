class SuperList(list):

    def __len__(self):
        return 1000



list1 = SuperList()
list1.append(3)
print(list1)
print(len(list1))
