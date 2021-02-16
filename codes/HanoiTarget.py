rods={'A':[1,2,3,4], 'B':[], 'C':[]}

def Hitogram(src, target):
    global rods
    rods[target].append(rods[src].pop())
    for i in rods:
        print i, rods[i]
    print '-'*10
    
def HanoiTower(src, target, by, num):
    if num==1:
        Hitogram(src, target)
        return 
    HanoiTower(src, by, target, num-1)
    HanoiTower(src, target, by, 1)
    HanoiTower(by, target, src, num-1)

if __name__=='__main__':
    HanoiTower('A', 'C', 'B', 4)