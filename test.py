if __name__ == '__main__':
    students=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append((score, name))
        
    students.sort()
    min_score = students[0][0] #Pega a menor nota
    second_min = None
    
    #Acha a segunda menor nota
    for score, name in students:
        if score > min_score:
            second_min = score
            break
    
    second_students = [name for score, name in students if score == second_min]
    second_students.sort()        
    
    for name in second_students:
        print(name)

