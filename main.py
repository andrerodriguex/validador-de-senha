import string
import getpass

def validar_senha():
    senha = getpass.getpass("Digite sua senha: ")
    strengh = 0
    remarks = ''
    lower_count = upper_count = num_count = wspace_count = special_count = 0

    for char in list(senha):
        if char in string.ascii_lowercase:
            lower_count += 1

        elif char in string.ascii_uppercase:
            upper_count += 1
        elif char in string.digits:
            num_count +=1
        elif char == ' ':
            wspace_count +=1
        else:
            special_count +=1
    
    if lower_count >= 1:
        strengh +=1
    if upper_count >= 1:
        strengh +=1
    if num_count >= 1:
        strengh +=1
    if wspace_count >= 1:
        strengh +=1
    if special_count >= 1:
        strengh +=1

    if strengh == 1:
        remarks = "Sua senha é muito fraca! Faça várias alterações."
    elif strengh == 2:
        remarks = "Sua senha é fraca! Adicione caracteres diferentes."
    elif strengh == 3:
        remarks = "Sua senha é fraca! Adicione caracteres diferentes."
    elif strengh == 4:
        remarks = "Sua senha é razoável, mas pode melhorar."
    elif strengh == 5:
        remarks = "Sua senha é ótima!"


    print('Sua senha tem: ')
    print(f"{lower_count} caracteres minúsculos")
    print(f"{upper_count} caracteres maiúsculos")
    print(f"{num_count} caracteres numerais")
    print(f"{wspace_count} caracteres em branco")
    print(f"{special_count} caracteres especiais")

    print(f"Força da senha: {strengh}")
    print(f"Dica: {remarks}")

def digitar_senha(outra_senha=False):
    valid = False
    if outra_senha:
        choice=input('Você quer digitar outra senha? (s/n): ')
    else:
        choice=input('Você quer mudar a força de sua senha? (s/n): ')

    while not valid:
        if choice.lower() == 's':
            return True
        elif choice.lower() == 'n':
            return False
        else:
            print('Resposta inválida, tente novamente.')

if __name__ == '__main__':
    print('Boas-vindas ao validador de senha forte!')
    valor_senha = digitar_senha()
    while validar_senha:
        validar_senha()
        valor_senha = digitar_senha(True)