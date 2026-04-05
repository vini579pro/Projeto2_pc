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

# --- ANALISE parte 2---

def analisarLog(nome_arq):
    # 1. Variáveis de contagem Geral
    total = 0
    sucesso = 0
    erro = 0
    erro500 = 0
    somaTempo = 0
    
    # 2. Métricas de Extremos e Distribução
    maiorTempo = 0
    menorTempo = 99999
    qtdRapidos = 0
    qtdNormais = 0
    qtdLentos = 0
    
    # 3. Distribuição de Status
    status200 = 0
    status403 = 0
    status404 = 0
    status500 = 0
    
    # 4. Frequência
    recursoMaisAcessado = "Processando..."
    ipMaisAtivo = "Processando..."
    ipComMaisErro = "Processando..."
    
    # 5. Segurança e Diagnóstico
    fb_eventos = 0
    fb_ultimo_ip = "Nenhum"
    fb_contador_seq = 0
    
    adm_indevidos = 0
    
    deg_eventos = 0
    deg_contador_seq = 0
    
    critica_eventos = 0
    critica_contador_seq = 0
    
    bot_eventos = 0
    bot_ultimo_ip = "Nenhum"
    bot_contador_seq = 0
    
    rota_sensivel_acessos = 0
    rota_sensivel_falhas = 0
    
    # Variáveis de controle para sequências (Estado anterior)
    ultimo_ip = ""
    ultimo_recurso = ""
    ultimo_status = ""
    ultimo_tempo_valor = 0

    try:
        with open(nome_arq, "r", encoding="UTF-8") as arq:
            for linha in arq:
                total += 1
                
                # --- EXTRAÇÃO MANUAL DOS CAMPOS (Requisito 11 - Proibido Split) ---
                ip = ""; metodo = ""; status = ""; recurso = ""; tempo_str = ""; agente = ""
                etapa = 0; p_inicial = 0
                
                # Pula a data [00/00/0000 00:00:00]
                for i in range(len(linha)):
                    if linha[i] == ']':
                        p_inicial = i + 2
                        break
                
                campo_atual = ""
                for i in range(p_inicial, len(linha)):
                    # Detecta o separador " - " manualmente
                    if linha[i:i+3] == " - ":
                        if etapa == 0: ip = campo_atual
                        elif etapa == 1: metodo = campo_atual
                        elif etapa == 2: status = campo_atual
                        elif etapa == 3: recurso = campo_atual
                        elif etapa == 4: tempo_str = campo_atual
                        elif etapa == 6: agente = campo_atual
                        campo_atual = ""
                        etapa += 1
                        # Pula os caracteres do separador " - "
                        
                    else:
                        # Lógica para não pegar caracteres de controle do separador
                        if not (linha[i-1:i+2] == " - " or linha[i-2:i+1] == " - "):
                            campo_atual += linha[i]

                # Limpeza do Tempo (remover 'ms')
                tempo_limpo = ""
                for c in tempo_str:
                    if c >= '0' and c <= '9': tempo_limpo += c
                tempo_int = int(tempo_limpo) if tempo_limpo != "" else 0

                # --- PROCESSAMENTO DE MÉTRICAS ---
                somaTempo += tempo_int
                
                # Maior e Menor Tempo
                if tempo_int > maiorTempo: maiorTempo = tempo_int
                if tempo_int < menorTempo: menorTempo = tempo_int
                
                # Classificação de Desempenho
                if tempo_int < 200: qtdRapidos += 1
                elif tempo_int < 800: qtdNormais += 1
                else: qtdLentos += 1
                
                # Status e Sucessos
                if status == "200":
                    sucesso += 1
                    status200 += 1
                else:
                    erro += 1
                    if status == "403": status403 += 1
                    elif status == "404": status404 += 1
                    elif status == "500": 
                        status500 += 1
                        erro500 += 1

                # --- ANÁLISES DE SEGURANÇA E PADRÕES ---
                
                # Força Bruta
                if ip == ultimo_ip and recurso == "/login" and status == "403":
                    fb_contador_seq += 1
                    if fb_contador_seq == 3:
                        fb_eventos += 1
                        fb_ultimo_ip = ip
                else:
                    fb_contador_seq = 1
                
                # Acesso Indevido ao /admin
                if recurso == "/admin" and status != "200":
                    adm_indevidos += 1
                
                # Degradação 
                if tempo_int > ultimo_tempo_valor and ultimo_tempo_valor > 0:
                    deg_contador_seq += 1
                    if deg_contador_seq == 3:
                        deg_eventos += 1
                else:
                    deg_contador_seq = 1
                
                # Falha Crítica : 3 erros 500 seguidos
                if status == "500" and ultimo_status == "500":
                    critica_contador_seq += 1
                    if critica_contador_seq == 3:
                        critica_eventos += 1
                else:
                    critica_contador_seq = 1
                
                # Detecção de Bot
                is_bot_agent = False
                if "Bot" in agente or "Crawler" in agente: is_bot_agent = True
                
                if ip == ultimo_ip:
                    bot_contador_seq += 1
                    if bot_contador_seq == 5 or is_bot_agent:
                        bot_eventos += 1
                        bot_ultimo_ip = ip
                else:
                    bot_contador_seq = 1
                
                # Rotas Sensíveis 
                if recurso == "/admin" or recurso == "/backup" or recurso == "/config" or recurso == "/private":
                    rota_sensivel_acessos += 1
                    if status != "200":
                        rota_sensivel_falhas += 1

                # Atualiza estados para a próxima linha
                ultimo_ip = ip
                ultimo_recurso = recurso
                ultimo_status = status
                ultimo_tempo_valor = tempo_int

        # --- CÁLCULOS FINAIS E RELATÓRIO
        if total > 0:
            disponibilidade = (sucesso / total) * 100
            taxaErro = (erro / total) * 100
            tempoMedio = somaTempo / total
        else:
            disponibilidade = taxaErro = tempoMedio = 0
            
        # Classificação do Estado Final 
        estado_final = "SAUDÁVEL"
        if critica_eventos >= 1 or disponibilidade < 70:
            estado_final = "CRÍTICO"
        elif disponibilidade < 85 or qtdLentos > (total * 0.3):
            estado_final = "INSTÁVEL"
        elif disponibilidade < 95 or fb_eventos > 0 or bot_eventos > 0:
            estado_final = "ATENÇÃO"

        # IMPRESSÃO DO RELATÓRIO COMPLETO
        print("\n" + "="*50)
        print("          RELATÓRIO FINAL - MONITOR LOGPY")
        print("="*50)
        print(f"Total de acessos: {total}")
        print(f"Total de sucessos (200): {sucesso}")
        print(f"Total de erros: {erro} | Erros críticos (500): {erro500}")
        print(f"Disponibilidade: {disponibilidade:.2f}%")
        print(f"Taxa de erro: {taxaErro:.2f}%")
        print(f"Tempo médio de resposta: {tempoMedio:.2f} ms")
        print(f"Maior tempo: {maiorTempo} ms | Menor tempo: {menorTempo} ms")
        print("-" * 50)
        print(f"DISTRIBUIÇÃO DE DESEMPENHO:")
        print(f" - Rápidos (<200ms): {qtdRapidos}")
        print(f" - Normais (200-799ms): {qtdNormais}")
        print(f" - Lentos (>=800ms): {qtdLentos}")
        print("-" * 50)
        print(f"DISTRIBUIÇÃO DE STATUS HTTP:")
        print(f" 200: {status200} | 403: {status403} | 404: {status404} | 500: {status500}")
        print("-" * 50)
        print(f"DIAGNÓSTICO DE SEGURANÇA E OPERAÇÃO:")
        print(f"Eventos de Força Bruta: {fb_eventos} (Último IP: {fb_ultimo_ip})")
        print(f"Acessos indevidos ao /admin: {adm_indevidos}")
        print(f"Eventos de degradação de desempenho: {deg_eventos}")
        print(f"Eventos de falha crítica: {critica_eventos}")
        print(f"Suspeitas de Bot: {bot_eventos} (Último IP: {bot_ultimo_ip})")
        print(f"Acessos a rotas sensíveis: {rota_sensivel_acessos} (Falhas: {rota_sensivel_falhas})")
        print("-" * 50)
        print(f"ESTADO FINAL DO SISTEMA: {estado_final}")
        print("="*50)
        
    except FileNotFoundError:
        print("[ERRO] Arquivo de log não encontrado. Gere os logs primeiro.")
    except Exception as e:
        print(f"[ERRO] Falha durante a análise: {e}")

menu()

    
    
