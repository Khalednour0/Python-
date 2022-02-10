
#<--------------------------------||member class||------------------------------------>
class member():
    #Functions
    def printPlayerData():
        pass

    def calcSalaryPerYear():
        pass

    def calcRemainingDuration():
        pass



#<-------------------------------||players class||------------------------------------>

#<<<<<<<<<<<<<<<<<<<<<<<<------Fields----->>>>>>>>>>>>>>>>>>>>>>>>>
class player(member):
    #Fields
    _playerName= None
    _playerNumber= None
    _playerSalary= 20000
    _signingDate= None
    _contractDuration= 3
    _numberMatches= 0
    _addYears=0


#<<<<<<<<<<<<<<<<<<<<<<------Get/set/delete----->>>>>>>>>>>>>>>>>>>>>>>
    
#<------------------//Player Name//--------------------->
    #getPlayerName
    def _get_playerName(self):
        return self._playerName
    #setPlayerName
    def _set_playerName(self,Name):
        self._playerName=Name
        return Name
    #delPlayerName
    def _del_playerName(self):
        print('You Cannot Delete This Element')

    playerName=property(_get_playerName,_set_playerName,_del_playerName)


#<-----------------//Player Number//------------------->     
    #setterPlayerNumber
    def __set_playerNumber(self,pNumber):
        self._playerNumber= pNumber
        while pNumber>30:
            if pNumber>30:
                print('Invalid Number it should be <30')
                pNumber=int(input('Enter Valid Number: '))
                self._playerNumber= pNumber
            else:
                self._playerNumber= pNumber

        self._playerNumber= pNumber
            
        
    #getPlayerNumber
    def _get_playerNumber(self):
        return self._playerNumber
    #setPlayerNumber
    def _set_playerNumber(self,pNumber):
        self._playerNumber=pNumber
        self.__set_playerNumber(pNumber)
        return self._playerNumber
    #delPlayerNumber
    def _del_playerNumber(self):
        print('You Cannot Delete This Element')

    playerNumber=property(_get_playerNumber,_set_playerNumber,_del_playerNumber)

    
#<-----------------//Player Salary//---------------------->       
    #setterPlayerSalary
    def __setter_playerSalary(self,salary):
        self._playerSalary=salary
        while salary>100000:
            if salary>100000:
                print('Invalid player salary it should be <100,000')
                salary=(int(input('Enter Valid salary: ')))
                self._playerSalary=salary
            else:
                self._playerSalary=salary

        self._playerSalary=salary
        
            
    #getSalary
    def __get_salaryPerYear(self):
        return self._playerSalary
    #setSalary
    def __set_salaryPerYear(self,salary):
        self.__setter_playerSalary(salary)
        return self._playerSalary
    #delSalary
    def __del_salaryPerYear(self):
        print('You Cannot Delete This Item')

    playerSalary=property(__get_salaryPerYear,__set_salaryPerYear,__del_salaryPerYear)

        
#<------------------//Player Signing Date//------------------>
    #getSigningDate
    def __get_signingDate(self):
        return self._signingDate
    #NonSet
    def __set_signingDate(self,date):
        print('You Cannot set this item \n'+ 'Date is: ' + str(self._signingDate))
    #delSigningDate
    def __del_signingDate(self):
        print('You Cannot Delete This Item')
        
    playerSigningDate=property(__get_signingDate,__set_signingDate,__del_signingDate)


#<---------------//Player Contract Duration//----------------->       
    #setterMaxContractDuration
    def __setter_maxContractDuration(self,duration):
        self._contractDuration=duration
        while duration>5:
            if duration>5:
                print('Invalid Contract Duration it should be <5')
                duration=int(input('Enter Valid Contract Duration: '))
                self._contractDuration=duration
            else:
                self._contractDuration=duration

        self._contractDuration=duration
        
            
    #getContractDuration        
    def __get_contractDuration(self):
        return self._contractDuration
    #setContractDuration
    def __Set_contractDuration(self,duration):
        self.__setter_maxContractDuration(duration)
        return self._contractDuration
    #delContractDuration
    def __del_contractDuration(self):
        print('You Cannot Delete This Item')
    
    playerContractDuration=property(__get_contractDuration,__Set_contractDuration,__del_contractDuration)


#<----------------//Player Number Matches//------------------>
    #getNumberMatches
    def __get_numberMatches(self):
        return self._numberMatches
    #setNumberMatches
    def __set_numberMatches(self,match):
        self._numberMatches=match
        return self._numberMatches
    #delNumberMatches
    def __del_numberMatches(self):
        print('You Cannot Delete This Item')
        
    playerNumberMacthes=property(__get_numberMatches,__set_numberMatches,__del_numberMatches)



#<<<<<<<<<<<<<<<<<<<<<<<<------Constructor----->>>>>>>>>>>>>>>>>>>>>>>>>
    #Constructor
    def __init__(self,pName,pNumber,sDate,pSalary=20000,pDuration=3,pNoMatches=0):
        self.__set_salaryPerYear(pSalary)
        self.__Set_contractDuration(pDuration)
        self.__set_numberMatches(pNoMatches)
        self.__set_playerNumber(pNumber)
        self._playerName= pName
        self._signingDate= sDate



#<<<<<<<<<<<<<<<<<<<<<<<<------FUNCTIONS----->>>>>>>>>>>>>>>>>>>>>>>>>
    #printPlayerData
    def printPlayerData(self):
        print('Player Name is: ', self._playerName)
        print('Player Number is: ', self._playerNumber)
        print('Player Signing Date is: ', self._signingDate)
        print('Player Salary Per Week is: ',self._playerSalary)
        print('Contract Duration in Years is: ',self._contractDuration)
        print('Number of Matches Played: ', self._numberMatches)
        

    #calcSalaryPerYear()
    def calcSalaryPerYear(self):
        totalSalary= self._playerSalary*4*12
        return totalSalary

    #calcRemainingDuration()
    def calcRemainingDuration(self):
        remDuration= self._signingDate+self._contractDuration-2022
        return str(remDuration)+' Year'

    #FIncreamentMatches()
    def IncreamentMatches(self):
        self._numberMatches+=1

    #increamentContractDutarion
    def increamentContractDutarion(self,_addYears=1):
        _addYears=int(input('Enter Additional Years: '))
        self._contractDuration+=_addYears


    #Overload"+"
    def __add__(x,y):
        z=x._playerSalary + y._playerSalary
        return z


#<----------------------------------||Captain Class||--------------------------------->

#<<<<<<<<<<<<<<<<<<<<<<------Fields----->>>>>>>>>>>>>>>>>>>>>>>
class captain(player):
    #Fields:
    _leadMatches=0
    _bonus=5000


#<<<<<<<<<<<<<<<<<<<<<<------Get/set/delete----->>>>>>>>>>>>>>>>>>>>>>>
    
#<-----------------//Captain Bonus//--------------------->
    #getBonus
    def __get_Bonus(self):
        return self._bonus
    #setBonus
    def __set_Bonus(self,bonus):
        self.__setter_Bonus(bonus)
        return bonus
    #delBonus
    def __del_bonus(self):
        self._bonus=0

    #setterCaptainBonus
    def __setter_Bonus(self,bonus):
        while bonus>100000:
            if bonus>100000:
                print('Invalid, Bonus should be < 100,000')
                bonus=(int(input('Enter Valid Bonus: ')))
                self._bonus=bonus
            else:
                self._bonus=bonus
        self._bonus=bonus
                
        
    CaptainBonus=property(__get_Bonus,__set_Bonus, __del_bonus)
    

#<----------------//Captain Lead Matches//----------------->
    #getLedMatches
    def __get_leadMatches(self):
        return self._leadMatches
    #NonSet
    def __set_leadMatches(self,match):
        print('You Cannot set this item \n'+ 'No. Lead Matches is: ' + str(self._leadMatches))

    leadMatches=property(__get_leadMatches,__set_leadMatches)
    


#<<<<<<<<<<<<<<<<<<<<<<<<------Constructor----->>>>>>>>>>>>>>>>>>>>>>>>>
    #Constructor
    def __init__(self,pName,pNumber,sDate,NoMatches=0,bonus=5000,pSalary=20000,pDuration=3,NoPlayed=0):
        super().__init__(pName,pNumber,sDate,pSalary,pDuration,NoPlayed)
        self._leadMatches=NoMatches
        self._bonus=bonus
        

#<<<<<<<<<<<<<<<<<<<<<<<<------FUNCTIONS----->>>>>>>>>>>>>>>>>>>>>>>>>   
    #printPlayerData
    def printPlayerData(self):
        player.printPlayerData(self)
        print('Number Of Matches Led is: ', self._leadMatches)
        print('Bonus is: ',self._bonus)
        print('')
        print(str(self._playerName)+ ' Is The Team Captain') 

    #Function calcSalaryPerYear()
    def calcSalaryPerYear(self):
        totalSalary= super().calcSalaryPerYear()+self._bonus
        return totalSalary

    #Function increamentLeadingMtaches()
    def increamentLeadingMtaches(self):
        self._leadMatches+=1



#<--------------------------------||Coach class||------------------------------------->

#<<<<<<<<<<<<<<<<<<<<<<------Fields----->>>>>>>>>>>>>>>>>>>>>>>
class coach(member):
    #Fields
    _coachName=None
    _coachSalary= 50000
    _coachDate=None
    _coachDuration= 2
    _coachExperience=None
    _coachBonus= 10000


#<<<<<<<<<<<<<<<<<<<<<<------Get/set/delete----->>>>>>>>>>>>>>>>>>>>>>>
    
#<-----------------//Coach Name//----------------------->
    #getCoachName
    def __get_coachName(self):
        return self._coachName
    #setCoachName
    def __set_coachName(self,cName):
        self._coachName= cName
        return self._coachName
    #delCoachName
    def __del_coacName(self):
        print('You Cannot Delete This Item')

    coachName=property(__get_coachName,__set_coachName,__del_coacName)
    

#<-----------------//Coach Salary//--------------------->
    #salaryConstrain
    def __setter_coachSalary(self,salary):
        while salary>200000:
            if salary>200000:
                print('Invalid Salary it should be < 200,000')
                salary=int(input('Enter Valid Coach Salary: '))
                self._coachSalary=salary 
            else:
                self._coachSalary=salary
                
        self._coachSalary=salary

    #getCoachSalary
    def __get_coachSalary(self):
        return self._coachSalary
    #setCoachSalary
    def __set_coachSalary(self,salary):
        self.__setter_coachSalary(salary)
        return self._coachSalary
    #delCoachSalary
    def __del_coachSalary(self):
        print('You Cannot Delete This Item')

    coachSalary=property(__get_coachSalary,__set_coachSalary,__del_coachSalary)

        
#<---------------//Coach Signing Date//------------------>
    #getCoachSigningDate
    def __get_coachSigningDate(self):
        return self._coachDate
    #setCoachSigningDate
    def __set_coachSigningDate(self,date):
        print('You Cannot set this item \n'+ 'Coach Signing Date is: ' + str(self._coachDate))
    #delCoachSigningDate
    def __del_coachSigningDate(self):
        print('You Cannot Delete This Item')

    coachSigningDate=property(__get_coachSigningDate,__set_coachSigningDate,__del_coachSigningDate)

            
#<-------------//Coach Contract Duration//---------------->
    #setterCoachContractDuratiion
    def __seteer_coachContractDuration(self,duration):
        while duration>3:
            if duration>3:
                print('Invalid, Contract Duration should be < 3 Years')
                duration=(int(input('Enter Valid Duration: ')))
                self._coachDuration=duration
            else:
                self._coachDuration=duration
                
        self._coachDuration=duration
            
    #getCoachContractDuration
    def __get_coachContractDuration(self):
        return self._coachDuration
    #setCoachContractDuration
    def __set_coachContractDuration(self,duration):
        self.__seteer_coachContractDuration(duration)
        return self._coachDuration
    #delCoachContractDuration
    def __del_coachContractDuration(self):
        print('You Cannot Delete This Item')

    coachContractDuration=property(__get_coachContractDuration,__set_coachContractDuration,__del_coachContractDuration)
        

#<--------------//Coach Experience//-------------------->
    #setterCoachExperience
    def __setter_coachExperience(self,exp):
        while exp<8:
            if exp<8:
                print('Invalid, Experience should be > 8 Years')
                exp=(int(input('Enter Valid Experience: ')))
                self._coachExperience=exp
            else:
                self._coachExperience=exp
                
        self._coachExperience=exp

    #getCoachExperience
    def __get_coachExperience(self):
        return self._coachExperience
    #setCoachExperience
    def __set_coachExperience(self,exp):
        print('You Cannot set this item \n'+ 'Coach Experience is: ' + str(self._coachExperience))
    #delCoachExperience
    def __del_coachExperience(self):
        print('You Cannot Delete This Item')

    coachExperience=property(__get_coachExperience,__set_coachExperience,__del_coachExperience)


#<---------------//Coach Bonus//------------------->
    #setterCoachBonus
    def __setter_coachBonus(self,bonus):
        while bonus>50000:
            if bonus>50000:
                print('Invalid, Bonus should be < 50,000')
                bonus=(int(input('Enter Valid Bonus: ')))
                self._coachBonus=bonus
            else:
                self._coachBonus=bonus
        self._coachBonus=bonus

    #getCoachBonus
    def __get_coachBonus(self):
        return self._coachBonus
    #setCoachBonus
    def __set_coachBonus(self,bonus):
       self.__setter_coachBonus(bonus)
       return self._coachBonus
    #delCoachBonus
    def __del_coachBonus(self):
        print('You Cannot Delete This Item')

    coachBonus=property(__get_coachBonus,__set_coachBonus,__del_coachBonus)
        

 
#<<<<<<<<<<<<<<<<<<<<<<<<------Constructor----->>>>>>>>>>>>>>>>>>>>>>>>>    
    #constructor
    def __init__(self,cName,cExp,cDate,salary=50000,duration=2,bonus=10000):    
        self.__setter_coachExperience(cExp)
        self._coachName= cName
        self._coachDate=cDate
        self.__setter_coachBonus(bonus)
        self.__seteer_coachContractDuration(duration)
        self.__setter_coachSalary(salary)
        
        

#<<<<<<<<<<<<<<<<<<<<<<<<------FUNCTIONS----->>>>>>>>>>>>>>>>>>>>>>>>>
    #Function printCoachData
    def printCoachData(self):
        print('Coach Name Is: ', self._coachName)
        print('Coach Experience is: ', self._coachExperience)
        print('Coach Signing Date: ' ,self._coachDate)
        print('Coach Salary is: ', self._coachSalary)
        print('Coach Bonus is: ', self._coachBonus)
        print('Coach Contract Duration is: ' , self._coachDuration)

    #Function IncreamentExperience Years
    def IncreamentExperienceYears(self):
        self._coachExperience += 1
        return self._coachExperience

    #Function Add Bonus
    def addBonus(self,bonus):
        self._coachBonus=bonus
        return 'Bonus Is ' +str(self._coachBonus)
        

#<-------------------------------||Team Class||--------------------------------------->
c=captain('Shenawy',0,2016)
#<<<<<<<<<<<<<<<<<<<<<<------Fields----->>>>>>>>>>>>>>>>>>>>>>>

class team():
    #Fields
    _teamName=None
    _teamPosition=None
    _teamCoach=None
    _playerList=[]
    _teamCaptain=None
    _numPlayers=0


#<<<<<<<<<<<<<<<<<<<<<<------Get/set/delete----->>>>>>>>>>>>>>>>>>>>>>>
    
#<-----------------//Team Name//------------------->
    #getTeamName
    def _get_teamName(self):
        return self._taemName
    #setTeamName
    def _set_teamName(self,tName):
        self._taemName=tName
    #delTeamName
    def _del_teamName(self):
        del self._taemName
        self._taemName=None

    teamName=property(_get_teamName,_set_teamName,_del_teamName)


#<-----------------//Team Position//------------------->
    #getTeamPosition
    def _get_teamPosition(self):
        return self._teamPosition
    #setTeamName
    def _set_teamPosition(self,tPosition):
        self._teamPosition=tPosition
    #delTeamName
    def _del_teamPosition(self):
        del self._teamPosition
        self._teamPosition=None

    teamPosition=property(_get_teamPosition,_set_teamPosition,_del_teamPosition)


#<-----------------//Team Coach//------------------->
    #getTeamCoach
    def _get_teamCoach(self):
        return self._teamCoach.printCoachData()
    #setTeamCoach
    def _set_teamCoach(self,tCoach):
        self._teamCoach=tCoach
    #delTeamCoach
    def _del_teamCoach(self):
        print('You Cannot Delete This Item')

    teamCoach=property(_get_teamCoach,_set_teamCoach,_del_teamCoach)


#<-----------------//Team Players List//------------------->
    #getPlayerList
    def _get_playerList(self):
        return self.printAllPlayers()
    #setPlayerList
    def _set_playerList(self,playerList):
        self._playerList=playerList
    #delPlayerList
    def _del_playerList(self):
        print('You Cannot Delete This Item')

    playerList=property(_get_playerList,_set_playerList,_del_playerList)


#<-----------------//Team Captain//------------------->
    #getTeamCaptain
    def _get_teamCaptain(self):
        self._modifyCaptain()
        self._teamCaptain.printPlayerData()
    #setTeamCaptain
    def _set_teamCaptain(self,tCaptain):
        self._teamCaptain=tCaptain
    #delTeamCaptain
    def _del_teamCaptain(self):
        print('You Cannot Delete This Item')

    teamCaptain=property(_get_teamCaptain,_set_teamCaptain,_del_teamCaptain)


#<-----------------//Team No. Players//------------------->
    #getNo.Players
    def _get_teamNoPlayers(self):
        return self._numPlayers
    #setNo.Players
    def _set_teamNoPlayers(self,numPlayers):
        print('You Cannot Set This Item')
    #delNo.Players
    def _del_teamNoPlayers(self):
        print('You Cannot Delete This Item')

    teamNoPlayers=property(_get_teamNoPlayers,_set_teamNoPlayers,_del_teamNoPlayers)

    
        
#<<<<<<<<<<<<<<<<<<<<<<<<------Constructor----->>>>>>>>>>>>>>>>>>>>>>>>>
    #Constructor
    def __init__(self,tCoach,tPosition,tName,tCaptain=c,playerList=[],numPlayers=0):
        self._teamCoach=tCoach
        self._taemName=tName
        self._teamPosition=tPosition
        self._teamCaptain=tCaptain
        self._playerList=playerList
        self._numPlayers=numPlayers
        


#<<<<<<<<<<<<<<<<<<<<<<<<------FUNCTIONS----->>>>>>>>>>>>>>>>>>>>>>>>>
    #print Team Data
    def printTeamData(self):
        print('<------------------Team--------------------->')
        print('Team Name Is: '+(self._taemName))
        print('Team Position Is: ' +str(self._teamPosition))
        print('Team No. Players Is: '+str(self._numPlayers))
        print('')
        self.printAllPlayers()
        print('<------------------Captain-------------------->')
        self._modifyCaptain()
        self._teamCaptain.printPlayerData()
        print('')
        print('<------------------Coach---------------------->')
        self._teamCoach.printCoachData()
        print('<--------------------------------------------->')
        
        
    #Print Captain Info    
    def printCaptainInfo(self):
        print('<------------------Captain-------------------->')
        self._modifyCaptain()
        self._teamCaptain.printPlayerData()
        



    def addPlayer(self,pName,pNumber,sDate,pSalary=20000,pContractDuration=3,pNoMatches=8):
        if self._playerList==[]:
            i=player(pName,pNumber,sDate,pSalary,pContractDuration,pNoMatches)
        else:
            for i in self._playerList:
                    f=False
                    if pNumber==i._playerNumber:
                        while f==False:
                            print('------There Is a Player With The Same Number------')
                            pNumber=int(input('Enter Another Number: '))
                            
                            if pNumber==i._playerNumber:
                                f=False
                            else:
                                f=True
                                
                            if f==True:
                                i=player(pName,pNumber,sDate,pSalary,pContractDuration,pNoMatches)
                                
                                if pNumber!=i._playerNumber:
                                    self._numPlayers+=1
                                 
                            else:
                                continue
                            
                    else:
                        i=player(pName,pNumber,sDate,pSalary,pContractDuration,pNoMatches)
               
                
        print('------------New Player Is Added------------')        
        self._playerList.append(i)
        self._numPlayers+=1
        print('no of Players is: '+str(self._numPlayers))



    
    #Print All Players                           
    def printAllPlayers(self):
        for i in self._playerList:
            print('------------Next Player-------------')
            i.printPlayerData()
            print('')


    #Modify Captain Info
    def _modifyCaptain(self):
        self._largestNoMatches()
        for i in self._playerList:
            if i._numberMatches==y:
                pName=i._playerName
                pNumber=i._playerNumber
                sDate=i._signingDate
                x=captain(pName,pNumber,sDate)
                self._teamCaptain=x
                
        
        

    def _largestNoMatches(self):
        l=[]
        for i in self._playerList:
            x=i._numberMatches
            l.append(x)
            l.sort()
        global y
        y=l[-1]



    #Delete player
    def delPlayer(self,pNumber):
        x=0
        for i in self._playerList:
            if pNumber==i._playerNumber:
                self._playerList.remove(i)
                self._numPlayers-=1
                print('------------------------------------------')
                print(str(i._playerName) + ' Is Kicked Out of The Team')
                print('no of Players is: '+str(self._numPlayers))
                print('------------------------------------------')
                x=1
                break
        if x==0:
            print('-----------------------------------------')
            print('no player exists with the given number')
            print('-----------------------------------------')
                        
        
    #Serch Player
    def serchPlayer(self,pNumber):
        x=0
        for i in self._playerList:
            if pNumber==i._playerNumber:
                i.printPlayerData()
                x=1
                break
        
        if x==0:
            print('-----------------------------------------')
            print('No Player Exist With This Number')
            print('-----------------------------------------')
            
            

    #Calc All Salary
    def calcAllSalary(self):
        x=0
        for i in self._playerList:
            x+=i._playerSalary

        y=x+coach._coachSalary
        print('------------------------------')
        print('Total Team Salary is: ' + str(y))
        print('------------------------------')

    #OverLoad __len__
    def __len__(self):
        print('-----------------------------------------')
        print('Number of Players in The Team is: '+str(self._numPlayers))
        print('-----------------------------------------')


    #OverLoad Indexer
    def __getitem__(self,pNumber):
        x=0
        for i in self._playerList:
            if pNumber==i._playerNumber:
                i.printPlayerData()
                return i._playerName
                x=1
                break
        if x==0:
            print('-----------------------------------------')
            print('No Player exists with this Number')
            print('-----------------------------------------')
            
            
        
        

        
#<<<<<<<<<<<<<<<<<<<<<<<<------RUN CODE----->>>>>>>>>>>>>>>>>>>>>>>>>
c=coach('Klopp',10,2017)
t=team(c,1,'Liverpool')
t.addPlayer('Van dijk',4,2017,pNoMatches=250)
t.addPlayer('Salah',11,2018,pNoMatches=200)
t.addPlayer('Mane',10,2016,pNoMatches=150)
t.addPlayer('Firmino',9,2018,pNoMatches=50)
print('\n')
t.__len__()
print('\n')
t.printCaptainInfo()
print('\n')
t.printTeamData()
print('\n')
t.calcAllSalary()
print('\n')
t.serchPlayer(10)
print('\n')
t[10]
print('\n')
t.delPlayer(10)
print('\n')
t.printCaptainInfo()
print('\n')
t.printTeamData()
print('\n')
t.__len__()
print('\n')
t.calcAllSalary()
            
        
            
            
        

   

            
            
        
        


        
        

                   


