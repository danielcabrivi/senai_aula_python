def calcular_resultado(nota1, nota2):
    # ====================================================
    # ÁREA DO ALUNO - AULA 04: MÉDIA ESCOLAR
    # ====================================================
    
    # 1. Lógica Matemática (Cálculo da Média)
    media = (nota1 + nota2) / 2
    
    # 2. Lógica Condicional (Aprovado / Recuperação / Reprovado)
    # Regras:
    # - Média >= 7.0 -> Aprovado (Verde)
    # - Média >= 5.0 -> Recuperação (Laranja)
    # - Menor que 5.0 -> Reprovado (Vermelho)

    situacao = "Indefinido"
    cor_visual = "cinza" # Opções: aprovado, recuperacao, reprovado

    if media >= 7.0:
        situacao = "APROVADO"
        cor_visual = "aprovado"
    elif media >= 5.0:
        situacao = "EM RECUPERAÇÃO"
        cor_visual = "recuperacao"
    else:
        situacao = "REPROVADO"
        cor_visual = "reprovado"

    # ====================================================
    # FIM DA ÁREA DO ALUNO
    # ====================================================
    
    return {
        "media_final": round(media, 1), # Arredonda para 1 casa decimal
        "status": situacao,
        "css": cor_visual
    }