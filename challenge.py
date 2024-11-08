from collections import deque

# Definição das linhas de metrô como listas 
metro_sp = {
    "Linha 1 - Azul": [
        "Jabaquara", "Conceição", "São Judas", "Saúde", "Praça da Árvore", 
        "Santa Cruz", "Vila Mariana", "Ana Rosa", "Paraíso", "Vergueiro", 
        "São Joaquim", "Liberdade", "Sé", "São Bento", "Luz", "Tiradentes", 
        "Armênia", "Portuguesa-Tietê", "Carandiru", "Santana", 
        "Jardim São Paulo-Ayrton Senna", "Parada Inglesa", "Tucuruvi"
    ],
    "Linha 2 - Verde": [
        "Vila Prudente", "Tamanduateí", "Sacomã", "Alto do Ipiranga", 
        "Santos-Imigrantes", "Chácara Klabin", "Ana Rosa", "Paraíso", 
        "Brigadeiro", "Trianon-Masp", "Consolação", "Clínicas", 
        "Sumaré", "Vila Madalena"
    ],
    "Linha 3 - Vermelha": [
        "Palmeiras-Barra Funda", "Marechal Deodoro", "Santa Cecília", 
        "República", "Anhangabaú", "Sé", "Brás", "Bresser-Mooca", 
        "Belém", "Tatuapé", "Carrão", "Penha", "Vila Matilde", 
        "Guilhermina-Esperança", "Patriarca", "Artur Alvim", 
        "Corinthians-Itaquera"
    ],
    "Linha 4 - Amarela": [
        "Luz", "República", "Higienópolis-Mackenzie", "Paulista", 
        "Fradique Coutinho", "Faria Lima", "Pinheiros", "Butantã", 
        "São Paulo-Morumbi", "Vila Sônia"
    ]
}

# Função para construir uma lista geral com todas as estações e conexões
def construir_grafo(metro):
    estacoes_das_linhas = {}
    
    for linha, estacoes in metro.items():
        for i in range(len(estacoes)):
            if estacoes[i] not in estacoes_das_linhas:
                estacoes_das_linhas[estacoes[i]] = []
            # Conectando a estação com as adjacentes
            if i > 0:
                estacoes_das_linhas[estacoes[i]].append(estacoes[i - 1])
            if i < len(estacoes) - 1:
                estacoes_das_linhas[estacoes[i]].append(estacoes[i + 1])
    
    return estacoes_das_linhas

# Algoritmo de busca para encontrar o menor caminho
def encontrar_caminho(metro, inicio, fim):
    estacoes_das_linhas = construir_grafo(metro)
    fila = deque([[inicio]])  # Fila com caminhos possíveis
    visitados = set()  # Conjunto de estações já visitadas

    while fila:
        caminho = fila.popleft()  # Pegamos o primeiro caminho da fila
        estacao_atual = caminho[-1]

        if estacao_atual == fim:  # Se chegamos ao destino
            return caminho

        elif estacao_atual not in visitados:
            visitados.add(estacao_atual)  # Marcamos a estação como visitada

            for vizinho in estacoes_das_linhas[estacao_atual]:  # Adicionamos as conexões (vizinhos)
                novo_caminho = list(caminho)
                novo_caminho.append(vizinho)
                fila.append(novo_caminho)
    
    return None  # Se não houver caminho

# Função para validar as entradas de estações
def validar_estacao(metro, estacao):
    estacoes = [est for linha in metro.values() for est in linha]
    return estacao in estacoes

# Função para cadastro de usuários
def cadastrar_usuario(usuarios):
    while True:
        nome = input("Digite o nome do usuário: ")
        email = input("Digite o e-mail do usuário: ")
        
        # Validação básica de e-mail
        if '@' not in email or '.' not in email:
            print("E-mail inválido. Tente novamente.")
            continue
        
        # Verifica se o usuário já está cadastrado
        if email in usuarios:
            print("Usuário já cadastrado.")
        else:
            usuarios[email] = {'nome': nome}
            print(f"Usuário {nome} cadastrado com sucesso!")
            break

# Função para login de usuários
def login(usuarios):
    email = input("Digite o e-mail para login: ")
    
    # Verifica se o e-mail está cadastrado
    if email in usuarios:
        print(f"Bem-vindo, {usuarios[email]['nome']}!")
        return email  # Retorna o e-mail do usuário logado
    else:
        print("Usuário não encontrado. Verifique o e-mail.")
        return None

# Função principal do menu de opções
def menu_principal():
    usuarios = {}
    usuario_logado = None

    while True:
        print("\n===== MENU PRINCIPAL =====")
        print("1. Cadastrar usuário")
        print("2. Login")
        print("3. Calcular caminho no metrô")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_usuario(usuarios)
        elif opcao == '2':
            usuario_logado = login(usuarios)
        elif opcao == '3':
            if usuario_logado:
                while True:
                    inicio = input("Digite a estação de início: ")
                    if not validar_estacao(metro_sp, inicio):
                        print("Estação de início inválida. Tente novamente.")
                        continue
                    
                    fim = input("Digite a estação de destino: ")
                    if not validar_estacao(metro_sp, fim):
                        print("Estação de destino inválida. Tente novamente.")
                        continue

                    caminho = encontrar_caminho(metro_sp, inicio, fim)
                    if caminho:
                        print(f"Caminho de {inicio} até {fim}: {' -> '.join(caminho)}")
                        print(f"Você deverá passar por {len(caminho) - 1} estações.")
                    else:
                        print(f"Não há caminho entre {inicio} e {fim}.")
                    break
            else:
                print("Você precisa estar logado para calcular um caminho.")
        elif opcao == '4':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Inicia o programa
menu_principal()
