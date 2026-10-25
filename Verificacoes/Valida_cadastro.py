from email_validator import validate_email,EmailNotValidError
def Valida_nome(nome:str):

    nome = nome.strip()

    if len(nome) < 3:
        return False

    if any(not char.isalpha() and char != " " for char in nome):
        return False

    return True

def Valida_cpf(cpf:str):

    def validacao_digito(cpf):
        soma = 0
        i = len(cpf)
        for char in cpf:
            soma += int(char)*(i+1)
            i -= 1

        return soma % 11
     
    if len(cpf) != 11:
        return False

    if not cpf.isnumeric():
        return False

    if all(char == cpf[0] for char in cpf):
        return False

    if validacao_digito(cpf[:9]) < 2:# primeiro  digito
        if int(cpf[9]) != 0:
            return False
    else:
        if int(cpf[9]) != 11 - validacao_digito(cpf[:9]):
            return False

    if validacao_digito(cpf[:10]) < 2:# segundo  digito
        if int(cpf[10]) != 0:
                return False
    else:
        if int(cpf[10]) != 11 - validacao_digito(cpf[:10]):
                return False

    return True

def Valida_email(email:str):

    try:
        validate_email(email)
        return True
    except EmailNotValidError:
        return False

def Valida_senha(senha:str):

    if len(senha)  < 8:
        return False

    if not (any(char.isnumeric() for char in senha) and any(char.isalpha() for char in senha)): # Verifica se tem letras e numeros
        return False

    if all(char.isalnum() for char in senha) or any(char.isspace() for char in senha): # Verifica se tem carcteres especiais sem espaco 
        return False

    if not any(char.isupper() for char in senha):
        return False
    

    return True
    
def confirma_senha(senha:str,confirma_senha:str):

    if not (senha == confirma_senha) or len(confirma_senha) == 0 :
        return False

    return True
