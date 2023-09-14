def solution(s):
    #holds index of all left arrows
    alllefts = []

    #holds index of all right arrows
    allrights = []

    #number of hellos exchanged
    hellos = 0



    #function to check if paths have crossed
    def crosscheck():
        i = 0
        crossed = 0
        while(i < len(allrights)):
            for j in range (len(alllefts)):
                if (alllefts[j] - allrights[i]) == 0 or (alllefts[j] - allrights[i]) == 1:
                    crossed = crossed + 2
            i = i + 1
    
        return crossed

    #function to move characters right and left
    def startmovin():
        for i in range (len(alllefts)):
            if alllefts[i] > 0:
                alllefts[i] -= 1
        for i in range (len(allrights)):
            if allrights[i] < len(s):
                allrights[i] += 1


    #Start here and check if both left and right movers exist. If not then hellos is zero
    if('<' and '>' in s):
        # Find all < and > and add to lists
        for i in range(len(s)):
            if s[i] == '<':
                alllefts.append(i)
            elif s[i] == '>':
                allrights.append(i)

        #check for hello exchanges before moving    
        hellos += crosscheck()
        
        while(alllefts[-1] > 0 and allrights[0] < len(s)):
            startmovin()
            hellos += crosscheck()

        return hellos
    else:
        return 0


        
    




        

           

            


        
        
        
        
        
        
        

