class Teams:
    def __init__(self, members):
        self.__myTeam = members

    def __len__(self):
        return len(self.__myTeam)
    
    def __contains__(self,m):
        return m in self.__myTeam
  
    def __iter__(self):
        self.x = 0
        return self

    def __next__(self):
        y = self.x
        self.x += 1
        if self.x > len(self.__myTeam):
            raise StopIteration
        return self.__myTeam[y]

        
def main():
    classmates = Teams(['John', 'Steve', 'Tim'])
    print (len(classmates))

    print ('Tim' in classmates)
    print ('Sam' in classmates)
  
    it = iter(classmates)
    # print (it)
    
    print (next(it))
    print (next(it))
    print (next(it))
    
    
main()

#Explain the difference between interfaces and implementation.
#
# Intefaces are the design of the class which contains the intructuions for the implementation
# The implementation is the actual instance of the class defined in the interface. The implemenation contains the logic where as the interface contains the design


# How would you design an interface structure such that all of the possible implementations could store data effectively.
#
# I design my inteface struces to be open to exention and closed for modifications have the generic "Save", "Connect", and "Read" method
# and then let each new storage method implement their own connection logic.
#
#