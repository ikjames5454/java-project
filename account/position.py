class Position:
    def sumAdd(self,element,val):
        return self.sort(element,val)

    def sort(self,element, value):
        for num in range(len(element)):
            for nums in range(1,len(element)):
                if element[num] + element[nums] == value:
                    return [num, nums]


    def sumUp(self,lis1,list2):
        new = []
        for element in range(len(lis1)):
            new.append(( lis1[element], list2[element]))
        return new

