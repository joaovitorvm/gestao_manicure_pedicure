import os

resp = 10

while (resp != 0): 
    os.system('cls || clear')
    mensagem = (r"""
 _   _         _  _               _
| \ | |       (_)| |             | |
|  \| |  __ _  _ | | ___  ______ | |__    ___   _ __ ___    ___
| . ` | / _` || || |/ __||______|| '_ \  / _ \ | '_ ` _ \  / _ \
| |\  || (_| || || |\__ \        | | | || (_) || | | | | ||  __/
|_| \_| \__,_||_||_||___/        |_| |_| \___/ |_| |_| |_| \___|
""")

    print(f" \033[1;35m {mensagem} \033[m ")

    print(f" \033[1;35m {"BOAS-VINDAS AO NAILS HOME  ^_^"} \033[m ")
    print()

    print(fr"{'=/'*17}\\")
    print(fr"|{'MODÚLO DE REGISTROS':.^34}|")
    print(fr"/|!/{'_'*30}\|")
    print(fr"/|{'_(1)-MODÚLO CLIENTES: _':.^32}\|")
    print(fr"/|{'_(2)-MODÚLO SERVIÇOS: _':.^32}\|")
    print(fr"/|{'_(3)-MODÚLO AGENDAMENTO: _':.^32}\|")
    print(fr"/|{'_(4)-MODÚLO RELATÓRIO: _':.^32}\|")
    print(fr"/|{'_(5)-MODÚLO SOBRE: _':.^32}\|")
    print(fr"/|{'_(0)-SAIR: _':.^32}\|")
    print(fr"/|!/{'_'*30}\!")
    print(fr"{'=/'*17}\\")
    print()
    resp = input("Selecione uma das opções: ")
    print()
    
    if resp == '1':
        os.system('cls || clear')
        print(fr"{'=/'*17}\\")
        print(fr"|{'MODÚLO CLIENTES':.^34}|")
        print(fr"/|!/{'_'*30}\|")
        print(fr"/|{'_(1)-CADASTRAR: _':.^32}\|")
        print(fr"/|{'_(2)-ATUALIZAR: _':.^32}\|")
        print(fr"/|{'_(3)-PESQUISAR: _':.^32}\|")
        print(fr"/|{'_(4)-EXCLUIR: _':.^32}\|")
        print(fr"/|{'_(0)-SAIR: _':.^32}\|")
        print(fr"/|!/{'_'*30}\!")
        print(fr"{'=/'*17}\\")
        print()
        resp1 = input("Selecione uma das opções: ")
        print()
        
        if resp1 == '1':
            os.system('cls || clear')
            print(f"{'=/'*17}\\")
            print(f" \033[1;35m {'CADASTRAR CLIENTES':.^34} \033[m ")
            print(fr"/|/{'-'*30}\|")
            nome = input("/|/>>Nome: ")
            print(fr"/|/{'='*30}\|")
            numero = input("/|/>>Número: ( ) ")
            print(fr"/|/{'-'*30}\|")
            contato = input("/|/>>Primeira vez: [S/N]").upper()
            print(fr"/(/{'-'*30}\)|")
            print()
            print(f" \033[1;35m {'Realizando cadastro...'} \033[m ")
            alerta =(r"""
            >>=====================<<
            ||   ESTE MODULO AINDA ||
            ||   SENDO PREPARADO   ||
            ||                     ||
            >>=====================<<
            """)
            print(f"\033[1;33m {alerta} \033[m ")
            print()
        elif resp1 == '2':
           os.system('cls || clear')
           print(f"{'=/'*17}\\")
           print(f" \033[1;35m {'ATUALIZAR CLIENTE':.^34} \033[m ")
           print(fr"/|/{'-'*30}\|")
           pesquisa = input("Insira o nome do cliente,\npara pesquisar o seu cadastro: ")
           print("Cliente encontrado, atualize seus dados!!")       
           nome = input("/|/>>Nome: ")
           print(fr"/|/{'='*30}\|")
           numero = input("/|/>>Número: ( ) ")
           print(fr"/|/{'-'*30}\|")
           contato = input("/|/>>Primeira vez: [S/N]").upper()
           print(fr"/(/{'-'*30}\)|")
           print()
           print(f" \033[1;35m {'Realizando atualizações...'} \033[m ")
           alerta =(r"""
            >>=====================<<
            ||   ESTE MODULO AINDA ||
            ||   SENDO PREPARADO   ||
            ||                     ||
            >>=====================<<
            """)
           print(f"\033[1;33m {alerta} \033[m ")
           print()         
        elif resp1 == '3':
           os.system('cls || clear')
           print(f"{'=/'*17}\\")
           print(f" \033[1;35m {'PESQUISAR CLIENTE':.^34} \033[m ")
           print(fr"/|/{'-'*30}\|")
           pesquisa = input("Insira o nome do cliente, \npara pesquisar: ")
           print("Cliente encontrado!!")       
           print(f"/|/>>Nome: {pesquisa}")
           print(fr"/|/{'='*30}\|")
           print("/|/>>Número: (84)98727-1562 ")
           print(fr"/|/{'-'*30}\|")
           print("/|/>>Primeira vez: [S]")
           print(fr"/(/{'-'*30}\)|")
           print()
           print(f" \033[1;35m {'Pesquisa concluida...'} \033[m ")
           alerta =(r"""
            >>=====================<<
            ||   ESTE MODULO AINDA ||
            ||   SENDO PREPARADO   ||
            ||                     ||
            >>=====================<<
            """)
           print(f"\033[1;33m {alerta} \033[m ")
           print()  
        elif resp1 == '4':
           os.system('cls || clear')
           print(f"{'=/'*17}\\")
           print(f" \033[1;35m {'EXCLUIR CLIENTE':.^34} \033[m ")
           print(fr"/|/{'-'*30}\|")
           excluir = input("Insira o nome do cliente, \npara excluir: ")
           print(f" \033[1;35m {'Cliente excluído':.^34} \033[m ")      
           print(fr"/(/{'-'*30}\)|")
           print()
           alerta =(r"""
            >>=====================<<
            ||   ESTE MODULO AINDA ||
            ||   SENDO PREPARADO   ||
            ||                     ||
            >>=====================<<
            """)
           print(f"\033[1;33m {alerta} \033[m ")
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
        

    elif resp == '2':
        print(fr"{'=/'*17}\\")
        print(fr"|{'MODÚLO SERVIÇOS':.^34}|")
        print(fr"/|!/{'_'*30}\|")
        print(fr"/|{'_(1)-CADASTRAR NOVO SERVIÇO _':.^32}\|")
        print(fr"/|{'_(2)-TABELA DE PREÇOS _':.^32}\|")
        print(fr"/|{'_(3)-ALTERAR _':.^32}\|")
        print(fr"/|{'_(4)-EXCLUIR _':.^32}\|")
        print(fr"/|{'_(0)-SAIR _':.^32}\|")
        print(fr"/|!/{'_'*30}\!")
        print(fr"{'=/'*17}\\")
        print()
        resp2 = input("Selecione uma das opções: ")
        print()
        if resp2 == '1':
            os.system('clear')
            print(f"{'=/'*17}\\")
            print(f" \033[1;35m {'CADASTRAR NOVO SERVIÇO':.^34} \033[m ")
            print(fr"/|!/{'-'*30}\|")
            servico = input("/|!/>>NOME DO SERVIÇO: ")
            print(fr"/|!/{'='*30}\|")
            valor = input("/|!/>>VALOR (R$): ")
            print(fr"/|!/{'-'*30}\|")
            tempo = input("/|!/>>DURAÇÃO ESTIMADA: ").upper()
            print(fr"/(/{'-'*30}\)|")
            print()
            print(f" \033[1;35m {'Serviço cadastrado ...'} \033[m ")
            alerta =(r"""
            >>=====================<<
            ||   ESTE MODULO AINDA ||
            ||   SENDO PREPARADO   ||
            ||                     ||
            >>=====================<<
            """)
            print(f"\033[1;33m {alerta} \033[m ")
            print()
        elif resp2 == '2':
           os.system('cls || clear')
           print(f"{'=/'*17}\\")
           print(f" \033[1;35m {'TABELA DE PREÇOS':.^34} \033[m ")
           print(fr"/|/{'-'*30}\|")
           print("Manicure Tradicional: R$ 35,00")
           print("Pedicure Tradicional: R$ 40,00")
           print("Combo Pé e Mão Completo: R$ 70,00") 
           print("Esmaltação Simples \n(Sem cutícula): R$ 20,00")  
           print(fr"/|/{'='*30}\|")
           alerta =(r"""
            >>=====================<<
            ||   ESTE MODULO AINDA ||
            ||   SENDO PREPARADO   ||
            ||                     ||
            >>=====================<<
            """)
           print(f"\033[1;33m {alerta} \033[m ")
           print()
        elif resp2 == '3':
           os.system('cls || clear')
           print(f"{'=/'*17}\\")
           print(f" \033[1;35m {'ALTERAR':.^34} \033[m ")
           print(fr"/|/{'-'*30}\|")
           servico = input("Insira o nome do serviço, \npara alterar:  ")      
           print(f"/|/>>Nome: {servico}")
           print(fr"/|/{'='*30}\|")
           preco = input("Informe o novo preço R$: ")
           print(fr"/(/{'-'*30}\)|")
           print()
           print(f" \033[1;35m {'alteração concluída...'} \033[m ")
           alerta =(r"""
            >>=====================<<
            ||   ESTE MODULO AINDA ||
            ||   SENDO PREPARADO   ||
            ||                     ||
            >>=====================<<
            """)
           print(f"\033[1;33m {alerta} \033[m ")
           print()  
        elif resp2 == '4':
           os.system('cls || clear')
           print(f"{'=/'*17}\\")
           print(f" \033[1;35m {'EXCLUIR SERVIÇO':.^34} \033[m ")
           print(fr"/|/{'-'*30}\|")
           excluir = input("Insira o nome do serviço, \npara excluir: ")
           print(f" \033[1;35m {'serviço excluído':.^34} \033[m ")      
           print(fr"/(/{'-'*30}\)|")
           print()
           alerta =(r"""
            >>=====================<<
            ||   ESTE MODULO AINDA ||
            ||   SENDO PREPARADO   ||
            ||                     ||
            >>=====================<<
            """)
           print(f"\033[1;33m {alerta} \033[m ")
           print()
        elif resp2 == '0':
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
        
        

            
    elif resp == '3':
        print(fr"{'=/'*17}\\")
        print(fr"|{'MODÚLO AGENDAMENTO':.^34}|")
        print(fr"/|!/{'_'*30}\|")
        print(fr"/|{'_(1)-AGENDAR NOVO HORÁRIO _':.^32}\|")
        print(fr"/|{'_(2)-VISUALIZAR AGENDA _':.^32}\|")
        print(fr"/|{'_(3)-ALTERAR HORÁRIO _':.^32}\|")
        print(fr"/|{'_(4)-CANCELAR _':.^32}\|")
        print(fr"/|{'_(5)-SAIR _':.^32}\|")
        print(fr"/|!/{'_'*30}\!")
        print(fr"{'=/'*17}\\")
        print()
        resp3 = input("Selecione uma das opções: ")
        print()
        if resp3 == '1':
            os.system('cls || clear')
            print(f"{'=/'*17}\\")
            print(f" \033[1;35m {'NOVO HORÁRIO':.^34} \033[m ")
            cliente = input("/|!/>>NOME DO CLIENTE: ")
            print(fr"/|!/{'-'*30}\|")
            servic = input("/|!/>>SERVIÇO DESEJADO: ")
            print(fr"/|!/{'-'*30}\|")
            horario = input("/|!/>>Informe o horário \n(HH:MM): ")
            print(fr"/|!/{'='*30}\|")
            dia = input("/|!/>>Informe  dia [SEG/TER/QUAR/\nQUINT/SEX/SAB]: ")
            print(fr"/(/{'-'*30}\)|")
            print()
            print(f" \033[1;35m {'Horário cadastrado...'} \033[m ")
            alerta =(r"""
            >>=====================<<
            ||   ESTE MODULO AINDA ||
            ||   SENDO PREPARADO   ||
            ||                     ||
            >>=====================<<
            """)
            print(f"\033[1;33m {alerta} \033[m ")
            print()
        elif resp3 == '2':
           os.system('cls || clear')
           print(f"{'=/'*17}\\")
           print(f" \033[1;35m {'VISUALIZAR HORÁRIO':.^34} \033[m ")
           print(fr"/|/{'-'*30}\|")
           print("Manicure Tradicional: R$ 35,00")
           print("Pedicure Tradicional: R$ 40,00")
           print("Combo Pé e Mão Completo: R$ 70,00") 
           print("Esmaltação Simples \n(Sem cutícula): R$ 20,00")  
           print(fr"/|/{'='*30}\|")
           alerta =(r"""
            >>=====================<<
            ||   ESTE MODULO AINDA ||
            ||   SENDO PREPARADO   ||
            ||                     ||
            >>=====================<<
            """)
           print(f"\033[1;33m {alerta} \033[m ")
           print()
           #falta 3,4
    elif resp == '4':
        os.system('cls || clear')
        print(fr"{'=/'*17}\\")
        print(fr"|{'MODÚLO RELATÓRIO':.^34}|")
        print(fr"/|!/{'_'*30}\|")
        print(fr"/|{'_(1)-FATURAMENTO TOTAL: _':.^32}\|")
        print(fr"/|{'_(2)-MEIOS DE PAGAMENTO: _':.^32}\|")
        print(fr"/|{'_(3)-CONTROLE DE DESPESAS: _':.^32}\|")
        print(fr"/|{'_(0)-SAIR: _':.^32}\|")
        print(fr"/|!/{'_'*30}\!")
        print(fr"{'=/'*17}\\")
        print()
        resp4 = input("Selecione uma das opções: ")
        print()     
    elif resp == '5':
        os.system('cls || clear')
        saida = (r"""
        >>======================<<
        || <<< MÓDULO SOBRE >>> ||
        **************************
        ||     OBRIGADO POR     ||
        ||UTILIZAR O GERENCIADOR||
        ||     NAILS HOUSE :)   ||
        >>======================<<
        """)
        print(f" \033[1;35m {saida} \033[m ")

    elif resp== '0':
        os.system('cls || clear')
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
            
            
    break

    #fim da primeira parte
    
    