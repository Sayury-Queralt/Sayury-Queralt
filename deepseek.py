if __name__ == '_main_':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append((score, name))  # Armazenando como tuplas (nota, nome)
    
    # Ordena a lista baseado nas notas (e depois nos nomes para desempate)
    students.sort()
    
    # Encontra a segunda menor nota
    min_score = students[0][0]
    second_min = None
    
    for score, name in students:
        if score > min_score:
            second_min = score
            break
    
    # Se todas as notas forem iguais, não há segunda menor
    if second_min is None:
        print("Todos os alunos têm a mesma nota.")
    else:
        # Filtra os alunos com a segunda menor nota e ordena alfabeticamente
        second_students = [name for score, name in students if score == second_min]
        second_students.sort()
        
        print("Os alunos com a segunda menor nota são:")
        for name in second_students:
            print(name)