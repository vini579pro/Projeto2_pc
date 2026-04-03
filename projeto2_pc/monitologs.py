import random
import datetime

def menu():
    nome_arq = "log.txt"
    
    while True:
        print('Monitor logPy')
        print("1 - gerar logs")
        print("2 - analisar logs")
        print("3 - gerar e analisar logs")
        print("4 - sair")
        
        opcao = input("escolha uma opcao:")
        
        if opcao == "1":
            try:
                qtd = int(input("quantidade de logs: "))
                gerarArquivo(nome_arq, qtd)
            except:
                print("qtd incorreta")
                
        elif opcao == "2":
            analisarLog(nome_arq)
            
        elif opcao == "3":
            try:
                qtd = int(input("quantidade de logs: "))
                gerarArquivo(nome_arq, qtd)
                analisarLog(nome_arq)
            except:
                print("qtd incorreta")
                
        elif opcao == "4":
            print("ate mais")
            break
        else:
            print("opcao errada")


def gerarArquivo(nome_arq, qtd):
    with open(nome_arq, "w", encoding="UTF-8") as arq:
        for i in range(qtd):
            arq.write(montarLog(i) + "\n")
    print("logs gerados")


def montarLog(i):
    data = gerarDataHora(i)
    ip = gerarIp(i)
    recurso = gerarRecurso(i)
    metodo = gerarMetodo(i)
    status = gerarStatus(i)
    tempo = gerarTempo(i)
    agente = gerarAgente(i)
    
    return f'[{data}] {ip} - {metodo} - {status} - {recurso} - {tempo}ms - 500B - HTTP/1.1 - {agente} - /home'


def gerarDataHora(i):
    base = datetime.datetime(2026,3,30,22,8,0)
    data = datetime.timedelta(seconds=i * random.randint(5,20))
    return (base + data).strftime("%d/%m/%Y %H:%M:%S")


def gerarIp(i):
    r = random.randint(1,6)
    
    if i >= 20 and i <= 30:
        return "200.0.111.345"
        
    if r == 1:
        return "192.168.5.8"
    elif r == 2:
        return "192.168.5.8"
    elif r == 3:
        return "192.168.5.9"
    elif r == 4:
        return "192.168.5.8"
    elif r == 5:
        return "192.168.25.8"
    else:
        return "192.168.65.68"


def gerarRecurso(i):
    r = random.randint(1,6)
    
    if i >= 20 and i <= 30:
        return "/login"
    
    if r == 1:
        return "/home"
    elif r == 2:
        return "/produtos"
    elif r == 3:
        return "/login"
    elif r == 4:
        return "/admin"
    elif r == 5:
        return "/backup"
    else:
        return "/config"


def gerarMetodo(i):
    if random.randint(1,2) == 1:
        return "GET"
    else:
        return "POST"


def gerarStatus(i):
    r = random.randint(1,6)
    
    if i >= 20 and i <= 30:
        return "403"
    
    if r == 1:
        return "200"
    elif r == 2:
        return "200"
    elif r == 3:
        return "404"
    elif r == 4:
        return "500"
    elif r == 5:
        return "403"
    else:
        return "200"


def gerarTempo(i):
    if i >= 40 and i <= 50:
        return str(200 + i * 10)
    
    return str(random.randint(100,1000))


def gerarAgente(i):
    r = random.randint(1,5)
    
    if r == 1:
        return "Chrome"
    elif r == 2:
        return "Firefox"
    elif r == 3:
        return "Edge"
    elif r == 4:
        return "BotCrawler"
    else:
        return "Safari"


#ANALISE

def analisarLog(nome_arq):
    total = 0
    sucesso = 0
    erro = 0
    erro500 = 0
    
    somaTempo = 0
    
    try:
        with open(nome_arq, "r", encoding="UTF-8") as arq:
            for linha in arq:
                total += 1
                
                # pegar status manual
                status = ""
                contador = 0
                
                for c in linha:
                    if c == "-":
                        contador += 1
                    elif contador == 2:
                        if c != " ":
                            status += c
                    elif contador > 2:
                        break
                
                # pegar tempo
                tempo = ""
                pegando = False
                
                for c in linha:
                    if c == "m":
                        break
                    if pegando:
                        tempo += c
                    if c == "-":
                        pegando = not pegando
                
                try:
                    tempo_int = int(tempo)
                except:
                    tempo_int = 0
                
                somaTempo += tempo_int
                
                if status == "200":
                    sucesso += 1
                else:
                    erro += 1
                    
                if status == "500":
                    erro500 += 1
        
        if total > 0:
            disponibilidade = (sucesso / total) * 100
            tempoMedio = somaTempo / total
        else:
            disponibilidade = 0
            tempoMedio = 0
        
        print("\n===== RELATORIO =====")
        print("total de acessos:", total)
        print("total de sucesso:", sucesso)
        print("total de erros:", erro)
        print("erros 500:", erro500)
        print("disponibilidade:", round(disponibilidade,2), "%")
        print("tempo medio:", round(tempoMedio,2), "ms")
        
    except:
        print("erro ao ler arquivo")


# iniciar
menu()
    
