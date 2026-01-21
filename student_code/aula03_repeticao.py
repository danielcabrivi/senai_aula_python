def gerar_inventario(qtd_desejada):
    # ====================================================
    # ÁREA DO ALUNO - AULA 03: REPETIÇÃO (LOOPS)
    # ====================================================
    
    lista_itens = []
    
    # O 'range' define quantas vezes o loop roda
    # 'i' é o contador (0, 1, 2, 3...)
    
    for i in range(qtd_desejada):
        
        # Lógica: A cada 5 itens, cria um Raro
        if (i % 5) == 0:
            nome_item = f"Cristal Raro #{i}"
        else:
            nome_item = f"Poção Comum #{i}"
            
        # Adiciona na lista
        lista_itens.append(nome_item)
    
    # ====================================================
    # FIM DA ÁREA DO ALUNO
    # ====================================================
    
    return {
        "lista": lista_itens,
        "total": len(lista_itens)
    }