import validacao

def menu_clientes(dados_clientes, grava_dados_clientes): 
    resp1 = ''
    while resp1 != '0': 
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print(f"|- \033[1;34m{'MÓDULO DE CLIENTES':^30}\033[m -|")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print("|-  (1) - Cadastrar Novo Cliente      -|")
        print("|-  (2) - Atualizar Cadastro          -|")
        print("|-  (3) - Pesquisar                   -|")
        print("|-  (4) - Excluir                     -|")
        print("|-  (0) - Sair                        -|")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print()
        resp1 = input("Escolha a opção desejada: ")
        
        if resp1 == '1':
            validacao.limpar()   
            print('='*36)
            print(f" \033[1;35m {'CADASTRAR CLIENTES':.^34} \033[m ")
            print('='*36)
            cpf = input("|-- CPF: ")
            valida_telefone = True
            while valida_telefone:
                print("Informe o número com DDD e 9 adicional\n(somente dígitos):")
                numero = input("|-- Número: ")
                if validacao.valida_telefone(numero):
                    print("Número válido!")
                    valida_telefone = False
                else:
                    print(f" \033[1;31m {'Não conseguimos validar seu número!\nVerifique os dados e tente novamente.'} \033[m ")
                    print()
            print("-" * 30)
            nome = input("|-- Nome: ")
            print("-" * 30)
            valida_email = True
            while valida_email:
                email = input("|-- E-mail: ")
                if validacao.validar_email(email):
                    print("E-mail válido!")
                    valida_email = False
                else:
                    print(f" \033[1;35m {'Não conseguimos validar seu Gmail!\nVerifique o formato e tente novamente.'} \033[m ")
                    print()
            print("=" * 36)
            aniversario = input("|-- Data de Nasc. (DD/MM): ")
            print("=" * 36)
            contato = input("|-- Primeira vez: [S/N] ").upper()
            print("=" * 36)
            print()
            dados_clientes[cpf] = [numero,nome,email,aniversario,contato,True]
            grava_dados_clientes(dados_clientes)
            print("Cliente: ",dados_clientes)
            print(f" \033[1;35m {'Realizando cadastro...'} \033[m ")
            alerta =(r"""
            >>============================<<
            ||   Cadastro Concluído!      ||
            || Dados salvos no sistema.   ||
            >>============================<<
            """)
            print()
            input("Tecle <ENTER> para continuar...")
        elif resp1 == '2':
            validacao.limpar()
            print('='*36)
            print(f" \033[1;35m {'ATUALIZAR CLIENTE':.^34} \033[m ")
            print('='*36)
            cpf_pesquisa = input("Insira o CPF do cliente para atualizar o cadastro: ")
            print()
            if cpf_pesquisa in dados_clientes:     
                print("|-- Dados atuais da cliente: ")
                print("|-- Numero: ", dados_clientes[cpf_pesquisa][0])
                print("|-- Nome: ", dados_clientes[cpf_pesquisa][1])
                print("|-- E-mail: ", dados_clientes[cpf_pesquisa][2], "--|")
                print("|-- Data de Nasc.: ", dados_clientes[cpf_pesquisa][3], "--|")
                print("|-- Primeira vez: ", dados_clientes[cpf_pesquisa][4],"--|")
                print("=" * 36)
                print()
                input("Tecle <ENTER> para continuar...")
                print()
        elif resp1 == '3':
           validacao.limpar()
           print('='*36)
           print(f" \033[1;35m {'PESQUISAR CLIENTE':.^34} \033[m ")
           print('='*36)
           cpf = input("Insira o cpf do cliente, \npara pesquisar: ")
           print()
           if cpf in dados_clientes:
               print(" \033[1;35m Dados cadastrados: \033[m ")
               print("|-- Numero: ",dados_clientes[cpf][0])
               print("|-- Nome: ",dados_clientes[cpf][1],"--|")
               print("|-- E-mail: ", dados_clientes[cpf][2], "--|")
               print("|-- Data de Nasc.: ", dados_clientes[cpf][3], "--|")
               print("|-- Primeira vez: ",dados_clientes[cpf][4],"--|")
               print()
           else:
              print()
              print(" \033[1;31m Cliente não encontrado no sistema! \033[m ")
              print()
           print(f" \033[1;35m {'Pesquisa concluida...'} \033[m ")
           alerta =(r"""
            >>============================<<
            ||   Pesquisa Concluída!      ||
            || Dados salvos no sistema.   ||
            >>============================<<
            """)
           print(f"\033[1;33m {alerta} \033[m ")
           print()
        elif resp1 == '4':
           validacao.limpar()
           print('='*36)
           print(f" \033[1;35m {'EXCLUIR CLIENTE':.^34} \033[m ")
           print('='*36)
           cpf = input("Insira o cpf do cliente, \npara excluir: ")
           if cpf in dados_clientes:
              print("|-- Dados atuais da cliente: ")  
              print("|-- Numero: ",dados_clientes[cpf][0])
              print("|-- Nome: ",dados_clientes[cpf][1])
              print("|-- E-mail: ", dados_clientes[cpf][2], "--|")
              print("|-- Data de Nasc.: ", dados_clientes[cpf][3], "--|")
              print("|-- Primeira vez: ",dados_clientes[cpf][4],"--|")
              print()

              verificar = input("Tecle 's' para confirmar exclusão...")
              if verificar.lower() == 's':
                  dados_clientes[cpf][5]=False
                  grava_dados_clientes(dados_clientes)
                  print(f" \033[1;33m {'Exclusão do cliente concluída...'} \033[m ")
                  print()
                  print("Cliente:",dados_clientes)
              else:
                  print(f" \033[1;35m {'exclusão cancelada ツ...'} \033[m ")
           else:
                  print(f" \033[1;33m {'Cliente não encontrado!'} \033[m ")
                  print()        

        elif resp1 == '0':
            saida = (r"""
            >>======================<<
            || <<< MÓDULO SAÍDA >>> ||
            **************************
            ||     OBRIGADO POR     ||
            ||UTILIZAR O GERENCIADOR||
            ||     NAILS HOUSE :)   ||
            >>======================<<
            """)     
            print(f" \033[1;35m {saida} \033[m ")
            input("Tecle <ENTER> para continuar...")