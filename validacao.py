def valida_telefone(numero):
    if len(numero) == 11 and numero.isdigit():
        return True   
    else:
        return False  
def validar_email(email):
    if "@gmail.com" in email:
        return True
    else:
        return False