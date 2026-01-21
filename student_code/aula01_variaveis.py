def configurar_personagem():
    # ====================================================
    # ÁREA DO ALUNO - AULA 01: VARIÁVEIS
    # ====================================================
    
    # 1. Strings (Texto)
    nome = "Dev Junior"
    classe = "Mago"
    
    # 2. Integers (Números Inteiros)
    # Tente mudar o HP para 20 e salve o arquivo!
    hp_atual = 100 
    hp_maximo = 100
    
    # 3. Boolean (Verdadeiro ou Falso)
    # Mude para False para desligar o brilho dourado
    modo_especial = True
    
    # ====================================================
    # FIM DA ÁREA DO ALUNO
    # ====================================================
    
    return {
        "nick": nome,
        "classe": classe,
        "hp": hp_atual,
        "max_hp": hp_maximo,
        "poder": modo_especial
    }