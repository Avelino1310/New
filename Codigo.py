
nomes = {
    "João": {"Matemática": [8.4, 10.0],
             "Português": [6.7, 4.3],
             "Inglês": [5.7, 9.2]
             },
    "Gabriel": {"Matemática": [8.4, 10.0],
                "Português": [6.7, 4.3],
                "Inglês": [5.7, 9.2]
                },
    "Davi": {"Matemática": [8.4, 10.0],
             "Português": [6.7, 4.3],
             "Inglês": [5.7, 8.2]
             }
}

def media_notas(nomes):
    print("\n=== Médias por Matéria ===")
    for aluno, materias in nomes.items():
        print(f"\nNotas de {aluno}:")
        for materia, notas in materias.items():
            media = sum(notas) / len(notas)
            print(f"  {materia}: {media:.2f}")
    print()

def media_total_aluno(nomes):
    print("\n=== Média Total por Aluno ===")
    medias_totais = {}
    for aluno, materias in nomes.items():
        todas_notas = []
        for notas in materias.values():
            todas_notas.extend(notas) 
        media = sum(todas_notas) / len(todas_notas)
        medias_totais[aluno] = media
        print(f"{aluno}: {media:.2f}")
    print()

def media_geral(nomes):
    print("\n=== Média Geral da Turma ===")
    notas_gerais = []
    for materias in nomes.values():
        for notas in materias.values():
            notas_gerais.extend(notas)
    media = sum(notas_gerais) / len(notas_gerais)
    print(f"Média geral da turma: {media:.2f}\n")

def menu():
    while True:
        print("=== MENU ===")
        print("1. Ver média por matéria (de cada aluno)")
        print("2. Ver média total por aluno")
        print("3. Ver média geral da turma")
        print("4. Sair\n")

        opcao = input("Escolha uma opção: ").strip()
        if opcao == "1":
            media_notas(nomes)
        elif opcao == "2":
            media_total_aluno(nomes)
        elif opcao == "3":
            media_geral(nomes)
        elif opcao == "4":
            print("\nEncerrando o sistema.")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

menu()
