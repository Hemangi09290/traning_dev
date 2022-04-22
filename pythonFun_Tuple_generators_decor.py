import os, re
from django.utils.timezone import datetime

class CricketScore:

    "match details cricketer name, position and his score"
    def __init__(self, cricketer, position,score):
        self.cricketer = cricketer
        self.poition = position
        self.score = score

    "use of tuple and its function"
    def get_score(self):
        score = (98,30,0)
        self.__init__("Sachin", 1, score[0])
        print("cricketer score")
        print(score)
        team_maxscore = max(score)
        print("Cricketer max score")
        print(team_maxscore)
        
    "use of generator and its function"
    "this is a simple function to show count of members in team"
    def get_teammembers(self):
        def mygen():
            i=11
            while i>0:
                yield i
                i-=1
        print("Total Team members in Team:")
        for i in mygen():
            print(i)
            
    "use of iterator"
    def get_iterativeScore(self):
        print("Iteration on Score:")
        score = (98,30,0)
        numIter=iter(score)
        print(numIter.__next__())
        print(next(numIter))
        print(numIter.__next__())
      
    def get_teamname(self, name):
        print("Playing Team Name:")
        iter_obj=iter(name)
        while True:
            try:
                i=next(iter_obj)
                print(i)
            except StopIteration:
                break
    
    "use of set {} function"
    def playDays(self):
        days={'Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'}
        print(len(days))
        set1,set2,set3={'Monday','Tuesday','Wednesday'},{'Wednesday','Thursday','Friday'},{'Friday','Saturday','Sunday'}
        print(set1.union(set2,set3))
    
CricketScore_obj1 = CricketScore("Sachin",1,96)
CricketScore_obj2 = CricketScore("Virat",2,93)
CricketScore_obj3 = CricketScore("kapil",3,90)

CricketScore_obj1.get_score()
CricketScore_obj1.get_teammembers()
CricketScore_obj1.get_iterativeScore()
CricketScore_obj1.get_teamname('MumbaiIndians')
CricketScore_obj1.playDays()
            
"use of decorator"
def decor1(func):
    def wrap():
        print("Price for winner team")
        func()
        print("Congratulations to Winning team")
    return wrap

def decor2(func):
    def wrap():
        print("Price for Man of the match")
        func()
        print("Congratulations to team player")
    return wrap
    
@decor1
@decor2
def sayhello():
    print("Hello")
    return "$500"

sayhello = decor1(sayhello)
sayhello()


