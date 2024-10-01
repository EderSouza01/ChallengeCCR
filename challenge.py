import requests

# Função para cadastro de usuários
def cadastrar_usuario(usuarios):
    nome = input("Digite o nome do usuário: ")
    email = input("Digite o e-mail do usuário: ")
    
    # Verifica se o usuário já está cadastrado
    if email in usuarios:
        print("Usuário já cadastrado.")
    else:
        usuarios[email] = {'nome': nome}
        print(f"Usuário {nome} cadastrado com sucesso!")

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

# Função para buscar informações do CEP
def buscar_cep():
    cep = input("Digite o CEP (com ou sem hífen): ")
    cep = cep.replace("-", "").strip()
    url = f"https://viacep.com.br/ws/{cep}/json/"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        dados = response.json()
        if "erro" not in dados:
            print(f"Endereço: {dados['logradouro']}, {dados['bairro']}, {dados['localidade']}-{dados['uf']}")
        else:
            print("CEP não encontrado.")
    else:
        print("Erro ao consultar o CEP.")

# Dicionário para armazenar os usuários
usuarios = {}

# Loop principal para cadastro e login
while True:
    acao = input("Deseja cadastrar (c) ou fazer login (l)? (s para sair): ")
    
    if acao.lower() == 'c':
        cadastrar_usuario(usuarios)
    elif acao.lower() == 'l':
        usuario_logado = login(usuarios)
        if usuario_logado:  # Se o login foi bem-sucedido
            while True:
                acao_cep = input("Deseja buscar um CEP (b) ou sair (s)? ")
                if acao_cep.lower() == 'b':
                    buscar_cep()
                elif acao_cep.lower() == 's':
                    print("Saindo do programa.")
                    break
                else:
                    print("Opção inválida. Tente novamente.")
    elif acao.lower() == 's':
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")

# Exibir todos os usuários cadastrados
print("\nUsuários cadastrados:")
for email, info in usuarios.items():
    print(f"Email: {email}, Nome: {info['nome']}")

