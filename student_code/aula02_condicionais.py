def verificar_acesso(senha_usuario):
    # ====================================================
    # ÁREA DO ALUNO - AULA 02: CONDICIONAIS
    # A variável 'senha_usuario' vem do Navegador!
    # ====================================================
    
    # Valores padrão (Caso a senha esteja errada)
    status_porta = "TRANCADA"
    cor_visual = "bloqueado" # Opções: 'bloqueado', 'liberado', 'alerta'
    mensagem = "Senha Incorreta"

    # LÓGICA DE VERIFICAÇÃO
    
    if senha_usuario == "admin":
        status_porta = "ABERTA (Admin)"
        cor_visual = "liberado"
        mensagem = "Acesso Total Concedido!"
        
    elif senha_usuario == "1234":
        status_porta = "ABERTA (Usuário)"
        cor_visual = "liberado"
        mensagem = "Bem-vindo de volta!"
        
    elif senha_usuario == "":
        status_porta = "ERRO"
        cor_visual = "alerta"
        mensagem = "Digite uma senha na URL!"
        
    # DESAFIO: Crie um 'elif' para a senha "senai"
    # elif senha_usuario == "senai":
    #    ...

    # ====================================================
    # FIM DA ÁREA DO ALUNO
    # ====================================================

    return {
        "status": status_porta,
        "css": cor_visual,
        "msg": mensagem
    }