if __name__ == '__main__':
    namel=[]
    scorel=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        namel.append(name)
        scorel.append(score)
        
    namet = tuple(namel)
    scoret = tuple(scorel)

    n = len(namet)
    minscore = float('inf')
    secscore = float('inf')
    secnamel = []

    for i in range(n): #achar o menor valor
        if scoret[i] < minscore:
            secscore = minscore
            minscore = scoret[i]

    for i in range(n): #achar o segundo menor valor
        if scoret[i] < secscore and scoret[i] > minscore:
            secscore = scoret[i]
            
        
    for i in range(n):
        if scoret[i] == secscore:
            secnamel.append(namet[i])


    secnamel.sort()
    print("Os alunos com a segunda menor nota são:")
    for i in secnamel:
        print(i)

