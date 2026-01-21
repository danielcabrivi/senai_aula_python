def validar_maioridade(idade_usuario):
    # ====================================================
    # ÁREA DO ALUNO - AULA 05: VERIFICADOR DE IDADE
    # ====================================================
    
    pode_entrar = False
    mensagem = "Analisando..."
    classe_css = "neutro" 

    # Lógica: Só entra se for MAIOR ou IGUAL a 18 anos
    
    if idade_usuario >= 18:
        pode_entrar = True
        mensagem = "ACESSO LIBERADO (+18)"
        classe_css = "liberado"
    else:
        pode_entrar = False
        mensagem = "ACESSO NEGADO (Menor de Idade)"
        classe_css = "bloqueado"

    # ====================================================
    # FIM DA ÁREA DO ALUNO
    # ====================================================

    return {
        "permitido": pode_entrar,
        "msg": mensagem,
        "css": classe_css
    }