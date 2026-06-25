import pickle
import validacao
import clientes
import servico
import subprocess


def recupera_dados_clientes():
    try:
        dados_clientes={}
        arqDados = open("dadosClientes.dat", "rb")
        dados_clientes = pickle.load(arqDados)
        arqDados.close()
    except:
        dados_clientes = { 
            '71100736450': ["João Vitor","joaovitorvenanciomedeiros@gmail.com","19/02/2008","S",True]
        }
        arqDados = open("dadosClientes.dat", "wb")
        pickle.dump(dados_clientes, arqDados)
        arqDados.close()
    return dados_clientes
dados_clientes = recupera_dados_clientes()
dados_servicos = {'1234' : ["Mão", "25.00", "1 hora"]}
try:
    arqServic = open("dadosService.dat", "rb")
    dados_servicos = pickle.load(arqServic)
    arqServic.close()
except:
    arqServic = open("dadosService.dat", "wb")
    pickle.dump(dados_servicos, arqServic) 
    arqServic.close()

dados_agendamentos = {'123' : ["84999000466","1234","09/06","16:45"]}
try:
    arqAgendamento = open("dadosAgendamento.dat", "rb")
    dados_agendamentos = pickle.load(arqAgendamento)
    arqAgendamento.close()
except:
    arqAgendamento = open("dadosAgendamento.dat", "wb")
    pickle.dump(dados_agendamentos, arqAgendamento) 
    arqAgendamento.close()

def grava_dados_clientes(dados_clientes):
    arqDados = open("dadosClientes.dat", "wb")
    pickle.dump(dados_clientes, arqDados)
    arqDados.close()

def grava_dados_servicos(dados_servicos):
    arqServic = open("dadosService.dat", "wb")
    pickle.dump(dados_servicos, arqServic)
    arqServic.close()

def grava_dados_agendamentos(dados_agendamentos): 
    arqAgendamento = open("dadosAgendamento.dat", "wb")
    pickle.dump(dados_agendamentos, arqAgendamento)
    arqAgendamento.close()


resp = '10'

while (resp != '0'): 
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
        clientes.menu_clientes(dados_clientes, grava_dados_clientes)
    elif resp == '2':
        servico.menu_servicos(dados_servicos, grava_dados_servicos)
    elif resp == '3':
        validacao.limpar()
        print(fr"{'=/'*17}\\")
        print(fr"|{'MODÚLO AGENDAMENTO':.^34}|") 
        print(fr"/|!/{'_'*30}\|")
        print(fr"/|{'_(1)-AGENDAR NOVO HORÁRIO _':.^32}\|")
        print(fr"/|{'_(2)-VISUALIZAR AGENDA _':.^32}\|")
        print(fr"/|{'_(3)-ALTERAR HORÁRIO _':.^32}\|")
        print(fr"/|{'_(4)-CANCELAR _':.^32}\|")
        print(fr"/|{'_(0)-SAIR _':.^32}\|")
        print(fr"/|!/{'_'*30}\!")
        print(fr"{'=/'*17}\\")
        print()
        resp3 = input("Selecione uma das opções: ")
        print()
        if resp3 == '1':
            validacao.limpar()
            print('='*36)
            print(f" \033[1;35m {'AGENDAR NOVO HORÁRIO':.^34} \033[m ")
            print('='*36)
            id_agendamento = input("Código do agendamento: ")
            print()
            print(" \033[1;35m Digite os dados do agendamento: \033[m ")
            cliente = input("|-- Nome do Cliente:     ")
            print('-' * 36)
            servico = input("|-- Serviço desejado:    ")
            print('-' * 36)
            dia = input("|-- Dia (Ex: SEG/SAB):   ")
            print('-' * 36)
            horario = input("|-- Horário (ex: 14:30): ")
            print('=' * 36)
            print()
            dados_agendamentos[id_agendamento] = [cliente, servico, dia, horario]
            print()
            print(f" \033[1;35m {'Horário cadastrado com sucesso...'} \033[m ")
            alerta =(r"""
            >>=====================<<
            ||   ESTE MODULO AINDA ||
            ||   SENDO PREPARADO   ||
            ||                     ||
            >>=====================<<
            """)
            print(f"\033[1;33m {alerta} \033[m ")
            print()
            input("Tecle <ENTER> para continuar...")
        elif resp3 == '2':
          validacao.limpar()
          print('='*36)
          print(f" \033[1;35m {'VISUALIZAR HORÁRIO':.^34} \033[m ")
          print('='*36)
          id_agendamento = input("Insira o Código do agendamento: ")
          print()
          if id_agendamento in dados_agendamentos:
            print(" \033[1;35m Dados da Marcação: \033[m ")
            print("|-- Cliente: ", dados_agendamentos[id_agendamento][0])
            print("|-- Serviço: ", dados_agendamentos[id_agendamento][1])
            print("|-- Dia:     ", dados_agendamentos[id_agendamento][2])
            print("|-- Horário: ", dados_agendamentos[id_agendamento][3])
            print("=" * 36)
            print()
          else:
            print(" \033[1;31m Agendamento não encontrado no sistema! \033[m ")
            print()
            print(f" \033[1;35m {'Pesquisa concluída...'} \033[m ")
          alerta =(r"""
          >>=====================<<
          ||   ESTE MODULO AINDA ||
          ||   SENDO PREPARADO   ||
          ||                     ||
          >>=====================<<
          """)
          print(f"\033[1;33m {alerta} \033[m ")
          print()
          input("Tecle <ENTER> para continuar...")
        elif resp3 == '3':
            validacao.limpar()
            print('='*36)
            print(f" \033[1;35m {'ALTERAR HORÁRIO':.^34} \033[m ")
            print('='*36)
            id_agendamento = input("Insira o Código do agendamento \npara alterar: ")
            print()
            if id_agendamento in dados_agendamentos:
               print(" \033[1;35m Dados da Marcação: \033[m ")             
               print("|-- Cliente: ", dados_agendamentos[id_agendamento][0])
               print("|-- Serviço: ", dados_agendamentos[id_agendamento][1])
               print("|-- Dia:     ", dados_agendamentos[id_agendamento][2])
               print("|-- Horário: ", dados_agendamentos[id_agendamento][3])
               print("=" * 36)
               print()
               print(" \033[1;35m Digite os novos dados: \033[m ")
               cliente = input("|-- Nome do Cliente:     ")
               print('-' * 36)
               servico = input("|-- Serviço desejado:    ")
               print('-' * 36)
               dia = input("|-- Dia (Ex: SEG/SAB):   ")
               print('-' * 36)
               horario = input("|-- Horário (ex: 14:30): ")
               print('=' * 36)
               dados_agendamentos[id_agendamento] = [cliente, servico, dia, horario]
               print()
               print(f" \033[1;35m {'Alteração concluída...'} \033[m ")
            else:
                print(" \033[1;31m Agendamento não encontrado no sistema! \033[m ")
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
            input("Tecle <ENTER> para continuar...")
        elif resp3 == '4':
            validacao.limpar()
            print('='*36)
            print(f" \033[1;35m {'CANCELAR HORÁRIO':.^34} \033[m ")
            print('='*36)
            id_agendamento = input("Insira o Código do agendamento \npara cancelar: ")
            print()
            if id_agendamento in dados_agendamentos:
               print(" \033[1;35m Dados da Marcação: \033[m ")             
               print("|-- Cliente: ", dados_agendamentos[id_agendamento][0])
               print("|-- Serviço: ", dados_agendamentos[id_agendamento][1])
               print("|-- Dia:     ", dados_agendamentos[id_agendamento][2])
               print("|-- Horário: ", dados_agendamentos[id_agendamento][3])
               print("=" * 36)
               print()
               verificar = input("Tecle 's' para confirmar exclusão...")
               if verificar.lower() == 's':
                  del dados_agendamentos[id_agendamento]
                  print(f" \033[1;33m {'Exclusão do agendamento concluída...'} \033[m ")
                  print()
                  print("Agendamento:",dados_agendamentos)  
               else:
                  print(f" \033[1;35m {'exclusão cancelada ツ...'} \033[m ")
            else:
                print(f" \033[1;33m {'Agendamento não encontrado!'} \033[m ")
                print()  
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
            input("Tecle <ENTER> para continuar...")
        elif resp3 == '0':
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
        

    elif resp == '4':
        validacao.limpar()
        print('='*36)
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
        if resp4 == '1':
           print('='*36)
           print(f" \033[1;35m {'FATURAMENTO TOTAL':.^34} \033[m ")
           print('='*36) 
    elif resp == '5':
        validacao.limpar()
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
        validacao.limpar()
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

    #fim da primeira parte

grava_dados_clientes(dados_clientes)
grava_dados_servicos(dados_servicos)
grava_dados_agendamentos(dados_agendamentos)

    
