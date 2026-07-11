import json
import os

PASTA_ATUAL = os.path.dirname(os.path.abspath(__file__))

ARQUIVO_JSON = os.path.join(PASTA_ATUAL, "biblioteca.json")
usuarios_cadastrados = os.path.join(PASTA_ATUAL, "usuarios.json")

# LISTA DE LIVROS
biblioteca = [
    {"id": 1, "titulo": "Dom Casmurro", "autor": "Machado de Assis", "avaliacao": 4.5, "estoque": 0},
    {"id": 2, "titulo": "Memórias Póstumas de Brás Cubas", "autor": "Machado de Assis", "avaliacao": 4.6, "estoque": 7},
    {"id": 3, "titulo": "Quincas Borba", "autor": "Machado de Assis", "avaliacao": 3.8, "estoque": 23},
    {"id": 4, "titulo": "Grande Sertão: Veredas", "autor": "Guimarães Rosa", "avaliacao": 3.7, "estoque": 23},
    {"id": 5, "titulo": "O Cortiço", "autor": "Aluísio Azevedo", "avaliacao": 4.8, "estoque": 2},
    {"id": 6, "titulo": "Vidas Secas", "autor": "Graciliano Ramos", "avaliacao": 4.4, "estoque": 1},
    {"id": 7, "titulo": "São Bernardo", "autor": "Graciliano Ramos", "avaliacao": 3.5, "estoque": 6},
    {"id": 8, "titulo": "A Hora da Estrela", "autor": "Clarice Lispector", "avaliacao": 3.8, "estoque": 19},
    {"id": 9, "titulo": "Perto do Coração Selvagem", "autor": "Clarice Lispector", "avaliacao": 3.5, "estoque": 6},
    {"id": 10, "titulo": "A Paixão Segundo G.H.", "autor": "Clarice Lispector", "avaliacao": 4.6, "estoque": 22},
    {"id": 11, "titulo": "Capitães da Areia", "autor": "Jorge Amado", "avaliacao": 4.3, "estoque": 7},
    {"id": 12, "titulo": "Gabriela, Cravo e Canela", "autor": "Jorge Amado", "avaliacao": 4.2, "estoque": 8},
    {"id": 13, "titulo": "Dona Flor e Seus Dois Maridos", "autor": "Jorge Amado", "avaliacao": 4.7, "estoque": 0},
    {"id": 14, "titulo": "Iracema", "autor": "José de Alencar", "avaliacao": 4.6, "estoque": 5},
    {"id": 15, "titulo": "O Guarani", "autor": "José de Alencar", "avaliacao": 4.5, "estoque": 10},
    {"id": 16, "titulo": "Senhora", "autor": "José de Alencar", "avaliacao": 3.9, "estoque": 6},
    {"id": 17, "titulo": "Triste Fim de Policarpo Quaresma", "autor": "Lima Barreto", "avaliacao": 4.9, "estoque": 10},
    {"id": 18, "titulo": "O Ateneu", "autor": "Raul Pompeia", "avaliacao": 3.7, "estoque": 12},
    {"id": 19, "titulo": "Macunaíma", "autor": "Mário de Andrade", "avaliacao": 3.6, "estoque": 11},
    {"id": 20, "titulo": "Vidas Secas", "autor": "Graciliano Ramos", "avaliacao": 4.4, "estoque": 25},
    {"id": 21, "titulo": "Angústia", "autor": "Graciliano Ramos", "avaliacao": 3.6, "estoque": 14},
    {"id": 22, "titulo": "O Quinze", "autor": "Rachel de Queiroz", "avaliacao": 4.3, "estoque": 12},
    {"id": 23, "titulo": "Ferreira Gullar: Poemas Escolhidos", "autor": "Ferreira Gullar", "avaliacao": 3.6, "estoque": 9},
    {"id": 24, "titulo": "Sentimento do Mundo", "autor": "Carlos Drummond de Andrade", "avaliacao": 4.7, "estoque": 19},
    {"id": 25, "titulo": "A Rosa do Povo", "autor": "Carlos Drummond de Andrade", "avaliacao": 4.8, "estoque": 11},
    {"id": 26, "titulo": "Torto Arado", "autor": "Itamar Vieira Junior", "avaliacao": 4.4, "estoque": 22},
    {"id": 27, "titulo": "A Bagagem", "autor": "Adélia Prado", "avaliacao": 3.6, "estoque": 21},
    {"id": 28, "titulo": "Relato de um Certo Oriente", "autor": "Milton Hatoum", "avaliacao": 3.8, "estoque": 9},
    {"id": 29, "titulo": "Dois Irmãos", "autor": "Milton Hatoum", "avaliacao": 5.0, "estoque": 7},
    {"id": 30, "titulo": "Cidade de Deus", "autor": "Paulo Lins", "avaliacao": 4.8, "estoque": 12},
    {"id": 31, "titulo": "1984", "autor": "George Orwell", "avaliacao": 3.9, "estoque": 20},
    {"id": 32, "titulo": "A Revolução dos Bichos", "autor": "George Orwell", "avaliacao": 4.8, "estoque": 5},
    {"id": 33, "titulo": "Cem Anos de Solidão", "autor": "Gabriel García Márquez", "avaliacao": 4.1, "estoque": 6},
    {"id": 34, "titulo": "O Amor nos Tempos do Cólera", "autor": "Gabriel García Márquez", "avaliacao": 4.5, "estoque": 22},
    {"id": 35, "titulo": "Crônica de uma Morte Anunciada", "autor": "Gabriel García Márquez", "avaliacao": 4.9, "estoque": 20},
    {"id": 36, "titulo": "Dom Quixote", "autor": "Miguel de Cervantes", "avaliacao": 3.6, "estoque": 20},
    {"id": 37, "titulo": "Guerra e Paz", "autor": "Liev Tolstói", "avaliacao": 3.8, "estoque": 23},
    {"id": 38, "titulo": "Anna Kariênina", "autor": "Liev Tolstói", "avaliacao": 3.9, "estoque": 14},
    {"id": 39, "titulo": "Crime e Castigo", "autor": "Fiódor Dostoiévski", "avaliacao": 4.1, "estoque": 20},
    {"id": 40, "titulo": "Os Irmãos Karamázov", "autor": "Fiódor Dostoiévski", "avaliacao": 4.5, "estoque": 7},
    {"id": 41, "titulo": "O Idiota", "autor": "Fiódor Dostoiévski", "avaliacao": 4.5, "estoque": 24},
    {"id": 42, "titulo": "A Metamorfose", "autor": "Franz Kafka", "avaliacao": 4.7, "estoque": 7},
    {"id": 43, "titulo": "O Processo", "autor": "Franz Kafka", "avaliacao": 4.7, "estoque": 25},
    {"id": 44, "titulo": "O Castelo", "autor": "Franz Kafka", "avaliacao": 4.0, "estoque": 8},
    {"id": 45, "titulo": "Ensaio Sobre a Cegueira", "autor": "José Saramago", "avaliacao": 3.6, "estoque": 18},
    {"id": 46, "titulo": "Memorial do Convento", "autor": "José Saramago", "avaliacao": 4.8, "estoque": 10},
    {"id": 47, "titulo": "O Evangelho Segundo Jesus Cristo", "autor": "José Saramago", "avaliacao": 3.8, "estoque": 15},
    {"id": 48, "titulo": "A Montanha Mágica", "autor": "Thomas Mann", "avaliacao": 4.1, "estoque": 20},
    {"id": 49, "titulo": "Ulysses", "autor": "James Joyce", "avaliacao": 4.2, "estoque": 8},
    {"id": 50, "titulo": "Retrato do Artista Quando Jovem", "autor": "James Joyce", "avaliacao": 3.7, "estoque": 23},
    {"id": 51, "titulo": "Mrs. Dalloway", "autor": "Virginia Woolf", "avaliacao": 4.3, "estoque": 8},
    {"id": 52, "titulo": "Rumo ao Farol", "autor": "Virginia Woolf", "avaliacao": 4.6, "estoque": 13},
    {"id": 53, "titulo": "Orlando", "autor": "Virginia Woolf", "avaliacao": 4.8, "estoque": 12},
    {"id": 54, "titulo": "O Grande Gatsby", "autor": "F. Scott Fitzgerald", "avaliacao": 4.0, "estoque": 4},
    {"id": 55, "titulo": "Suave é a Noite", "autor": "F. Scott Fitzgerald", "avaliacao": 4.3, "estoque": 2},
    {"id": 56, "titulo": "O Sol Também se Levanta", "autor": "Ernest Hemingway", "avaliacao": 4.6, "estoque": 3},
    {"id": 57, "titulo": "O Velho e o Mar", "autor": "Ernest Hemingway", "avaliacao": 3.7, "estoque": 5},
    {"id": 58, "titulo": "Adeus às Armas", "autor": "Ernest Hemingway", "avaliacao": 4.7, "estoque": 13},
    {"id": 59, "titulo": "As Vinhas da Ira", "autor": "John Steinbeck", "avaliacao": 4.4, "estoque": 12},
    {"id": 60, "titulo": "A Leste do Éden", "autor": "John Steinbeck", "avaliacao": 4.1, "estoque": 14},
    {"id": 61, "titulo": "Ratos e Homens", "autor": "John Steinbeck", "avaliacao": 4.3, "estoque": 17},
    {"id": 62, "titulo": "Moby Dick", "autor": "Herman Melville", "avaliacao": 4.8, "estoque": 0},
    {"id": 63, "titulo": "Orgulho e Preconceito", "autor": "Jane Austen", "avaliacao": 4.5, "estoque": 3},
    {"id": 64, "titulo": "Razão e Sensibilidade", "autor": "Jane Austen", "avaliacao": 4.5, "estoque": 17},
    {"id": 65, "titulo": "Emma", "autor": "Jane Austen", "avaliacao": 4.6, "estoque": 24},
    {"id": 66, "titulo": "Grandes Esperanças", "autor": "Charles Dickens", "avaliacao": 4.5, "estoque": 3},
    {"id": 67, "titulo": "Oliver Twist", "autor": "Charles Dickens", "avaliacao": 3.9, "estoque": 5},
    {"id": 68, "titulo": "Um Conto de Natal", "autor": "Charles Dickens", "avaliacao": 4.2, "estoque": 23},
    {"id": 69, "titulo": "David Copperfield", "autor": "Charles Dickens", "avaliacao": 4.8, "estoque": 8},
    {"id": 70, "titulo": "O Morro dos Ventos Uivantes", "autor": "Emily Brontë", "avaliacao": 5.0, "estoque": 24},
    {"id": 71, "titulo": "Jane Eyre", "autor": "Charlotte Brontë", "avaliacao": 3.8, "estoque": 3},
    {"id": 72, "titulo": "Os Miseráveis", "autor": "Victor Hugo", "avaliacao": 4.8, "estoque": 9},
    {"id": 73, "titulo": "O Corcunda de Notre-Dame", "autor": "Victor Hugo", "avaliacao": 4.8, "estoque": 16},
    {"id": 74, "titulo": "Madame Bovary", "autor": "Gustave Flaubert", "avaliacao": 4.4, "estoque": 4},
    {"id": 75, "titulo": "O Retrato de Dorian Gray", "autor": "Oscar Wilde", "avaliacao": 4.1, "estoque": 5},
    {"id": 76, "titulo": "Frankenstein", "autor": "Mary Shelley", "avaliacao": 4.3, "estoque": 24},
    {"id": 77, "titulo": "Drácula", "autor": "Bram Stoker", "avaliacao": 4.9, "estoque": 0},
    {"id": 78, "titulo": "O Médico e o Monstro", "autor": "Robert Louis Stevenson", "avaliacao": 4.4, "estoque": 15},
    {"id": 79, "titulo": "A Ilha do Tesouro", "autor": "Robert Louis Stevenson", "avaliacao": 3.5, "estoque": 11},
    {"id": 80, "titulo": "Vinte Mil Léguas Submarinas", "autor": "Júlio Verne", "avaliacao": 4.8, "estoque": 25},
    {"id": 81, "titulo": "A Volta ao Mundo em 80 Dias", "autor": "Júlio Verne", "avaliacao": 4.0, "estoque": 1},
    {"id": 82, "titulo": "Viagem ao Centro da Terra", "autor": "Júlio Verne", "avaliacao": 3.9, "estoque": 18},
    {"id": 83, "titulo": "A Peste", "autor": "Albert Camus", "avaliacao": 4.9, "estoque": 2},
    {"id": 84, "titulo": "O Estrangeiro", "autor": "Albert Camus", "avaliacao": 4.6, "estoque": 2},
    {"id": 85, "titulo": "A Náusea", "autor": "Jean-Paul Sartre", "avaliacao": 5.0, "estoque": 17},
    {"id": 86, "titulo": "O Apanhador no Campo de Centeio", "autor": "J.D. Salinger", "avaliacao": 4.6, "estoque": 4},
    {"id": 87, "titulo": "Lolita", "autor": "Vladimir Nabokov", "avaliacao": 4.5, "estoque": 17},
    {"id": 88, "titulo": "Admirável Mundo Novo", "autor": "Aldous Huxley", "avaliacao": 3.7, "estoque": 16},
    {"id": 89, "titulo": "Fahrenheit 451", "autor": "Ray Bradbury", "avaliacao": 4.8, "estoque": 13},
    {"id": 90, "titulo": "O Sol é Para Todos", "autor": "Harper Lee", "avaliacao": 4.9, "estoque": 17},
    {"id": 91, "titulo": "A Insustentável Leveza do Ser", "autor": "Milan Kundera", "avaliacao": 4.6, "estoque": 22},
    {"id": 92, "titulo": "O Nome da Rosa", "autor": "Umberto Eco", "avaliacao": 3.8, "estoque": 9},
    {"id": 93, "titulo": "Sidarta", "autor": "Hermann Hesse", "avaliacao": 4.1, "estoque": 21},
    {"id": 94, "titulo": "O Lobo da Estepe", "autor": "Hermann Hesse", "avaliacao": 4.5, "estoque": 14},
    {"id": 95, "titulo": "A Divina Comédia", "autor": "Dante Alighieri", "avaliacao": 4.8, "estoque": 14},
    {"id": 96, "titulo": "Fausto", "autor": "Johann Wolfgang von Goethe", "avaliacao": 3.7, "estoque": 7},
    {"id": 97, "titulo": "Os Sofrimentos do Jovem Werther", "autor": "Johann Wolfgang von Goethe", "avaliacao": 3.6, "estoque": 0},
    {"id": 98, "titulo": "O Senhor dos Anéis: A Sociedade do Anel", "autor": "J.R.R. Tolkien", "avaliacao": 4.4, "estoque": 7},
    {"id": 99, "titulo": "O Senhor dos Anéis: As Duas Torres", "autor": "J.R.R. Tolkien", "avaliacao": 4.4, "estoque": 0},
    {"id": 100, "titulo": "O Senhor dos Anéis: O Retorno do Rei", "autor": "J.R.R. Tolkien", "avaliacao": 3.6, "estoque": 20},
]
# =====================================
# SALVAR E CARREGAR DADOS
# =====================================
def salvar_biblioteca(biblioteca):
    with open(ARQUIVO_JSON, "w", encoding="utf-8") as f:
        json.dump(biblioteca, f, ensure_ascii=False, indent=4)

def carregar_biblioteca(biblioteca_padrao):
    if os.path.exists(ARQUIVO_JSON):
        with open(ARQUIVO_JSON, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        # primeira vez rodando: cria o arquivo com os dados padrão
        salvar_biblioteca(biblioteca_padrao)
        return biblioteca_padrao

biblioteca = carregar_biblioteca(biblioteca)

usuarios = []

# =====================================
# SALVAR E CARREGAR DADOS
# =====================================
def salvar_usuarios(usuarios):
    with open(usuarios_cadastrados, "w", encoding="utf-8") as f:
        json.dump(usuarios, f, ensure_ascii=False, indent=4)

def carregar_usuarios(usuarios):
    if os.path.exists(usuarios_cadastrados):
        with open(usuarios_cadastrados, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        # primeira vez rodando: cria o arquivo com os dados padrão
        salvar_usuarios(usuarios)
        return usuarios

usuarios = carregar_usuarios(usuarios)

# ========================
# FUNÇÃO P/ CADASTRAR
# ========================= 
def cadastrar_usuario(usuarios):
    nome_usuario = input("Crie seu nome de usuario: ")

    for nome in usuarios:
        if nome_usuario == nome['nome_usuario']:
            print("Nome inválido")
            return
# USUARIO DIGITAR SENHA
    senha_usuario = input("Digite sua senha: ")
    novo_usuario = {"nome_usuario": nome_usuario, "senha": senha_usuario, "livros_emprestados": []}
    usuarios.append(novo_usuario)
    salvar_usuarios(usuarios)
    return novo_usuario

# ========================
# FUNÇÃO P/ LOGAR NOVO USER
# ========================= 
def logar_usuario(usuarios):
    print("Digite seu nome de usuário e senha para entrar na conta.")
    nome_usuario = input("Nome de usuario: ")
    senha_usuario = input("Senha: ")

    for usuario in usuarios:
        if nome_usuario == usuario['nome_usuario'] and senha_usuario == usuario['senha']:
            print("Login feito com sucesso!")
            return usuario
    print("Senha ou nome errado")

# =====================================
# FUNÇÃO P/ RESERVAR LIVROS
# =====================================
def pegar_livro(biblioteca, usuario_logado,usuarios):
    while True:
        try:
            id_livro = int(input("Qual livro deseja pegar emprestado? (Responda com o número referente ao livro desejado. Ex: 1)") )
        except ValueError:
            print("Digite apenas NÚMEROS!")
            continue 

        livro_encontrado = False
        for livro in biblioteca:
            if livro['id'] == id_livro:
                livro_encontrado = True
                if livro['estoque'] == 0:
                    print("Sem estoque do livro no momento, volte outro dia.")
                    break
                else:
                    livro['estoque'] -= 1
                    print("Livro reservado com sucesso. Você tem até 30 dias para devolver ou renovar o tempo de empréstimo.")
                    salvar_biblioteca(biblioteca)
                    usuario_logado['livros_emprestados'].append(id_livro)
                    salvar_usuarios(usuarios)
                    return
        if not livro_encontrado:
            print("Livro indisponível!")
        continue

# ========================
# FUNÇÃO P/ LISTAR LIVROS
# =========================
def listar_livros(biblioteca, usuario_logado, usuarios):
    for livro in biblioteca:
        print(f"{livro['id']}. {livro['titulo']} - {livro['autor']} | Avaliação: {livro['avaliacao']} | Estoque: {livro['estoque']}")
    resposta = input("Deseja pegar algum livro emprestado? (responda com SIM ou NÃO)")

    if resposta.upper() == "SIM":
        pegar_livro(biblioteca, usuario_logado, usuarios)
    else:
        print("Voltando para o menu principal.")
# ===========================================
# FUNÇÃO P/ PROCURAR LIVROS POR AUTOR/TITULO
# =============================================
def procura_exata(biblioteca, campo, termo, usuario_logado, usuarios):
    resultados = []

    for livro in biblioteca:
        if termo.lower() in livro[campo].lower():
            resultados.append(livro)
    if resultados:   
        print(f"{len(resultados)} resultado(s) encontrado(s)")
        for livro in resultados:
            print(f"{livro['id']}. {livro['titulo']} - {livro['autor']} | Avaliação: {livro['avaliacao']} | Estoque: {livro['estoque']}")
        
        resposta = input("Deseja pegar algum livro? (responda com SIM ou NÃO)")
        if resposta.upper() == "SIM":
            pegar_livro(biblioteca, usuario_logado, usuarios)
        else:
            print("Voltando para o menu principal.")
    else:
        print("Nenhum resultado encontrado")

# ===========================
# MENU PARA PROCURA DE LIVROS
# ============================
def procurar_livro(biblioteca, usuario_logado, usuarios):
    print("=======================================")
    print("          PROCURA DE LIVROS            ")
    print("=======================================")
    print("1. Procurar por autor")
    print("2. Procurar por título")
    opcao = input("O que deseja? ")

    if opcao == "1":
        autor = input("Digite o nome de autor: ")
        procura_exata(biblioteca, "autor", autor, usuario_logado, usuarios)
    elif opcao == "2":
        titulo = input("Digite o título do livro: ")
        procura_exata(biblioteca, "titulo", titulo, usuario_logado, usuarios)
    else: 
        print("Opção inválida!")

# ===========================
# FUNÇÃO P/ DEVOLVER LIVROS
# ============================
def devolver_livro(biblioteca, usuario_logado, usuarios):
    print("=================================")
    print("       DEVOLUÇÃO DE LIVROS       ")
    print("=================================")
    print("A devolução de livros e feita por meio de ID. Pode achar os ID's na lista de livros.")
    livros_com_usuario = []
    for id in usuario_logado['livros_emprestados']:
        for livro in biblioteca:
            if livro['id'] == id:
                livros_com_usuario.append(f"{livro['id']} - {livro['titulo']} - {livro['autor']}")
                
    print(f"ID's dos livros com você: " )
    if len(livros_com_usuario) == 0:
        print("Você está sem livros.")
    else: 
        for livro in livros_com_usuario:
            print(livro)
    while True:
        try:
            id_livro = int(input("Digite o id do livro a ser devolvido: "))
        except ValueError:
            print("ID inválido! Tente novamente.") 
            continue

        livro_encontrado = False
        for livro in biblioteca:
            if id_livro == livro['id']:
                livro_encontrado = True
                print("Resultado: ")
                print(f"{livro['titulo']} - {livro['autor']}")
                print(" ")

                resposta = input("Confirma devolver o livro? (Responda com SIM ou NÃO)")

                if resposta.upper() == "SIM":
                    if id_livro not in usuario_logado['livros_emprestados']:
                        print("Esse livro não consta como emprestado na sua conta.")
                        return
                    livro['estoque'] += 1
                    usuario_logado['livros_emprestados'].remove(id_livro)
                    salvar_biblioteca(biblioteca)
                    salvar_usuarios(usuarios)
                    print("Livro devolvido com sucesso.")
                    return
                else:
                    print("Voltando...")
                    return
        if not livro_encontrado:
            print("ID não encontrado!")
            continue

# ========================
# LOOP P/ FAZER LOGIN
# ========================= 
while True:
    print("=======================================")
    print("             BIBLIOTECA                ")
    print("=======================================") 
    print("1. Logar")
    print("2. Cadastrar")           
    opcao = input("O que deseja fazer? ")

    if opcao == "1":
        usuario_logado = None
        while usuario_logado is None:
            usuario_logado = logar_usuario(usuarios)
        break
    elif opcao == "2":
        cadastrar_usuario(usuarios)
    else:
        print("Opção inválida")
        continue
    
# ========================
# LOOP INICIAL (MENU)
# =========================
while True:
    print("=======================================")
    print("             BIBLIOTECA                ")
    print("=======================================")
    print("1. Listar livros")
    print("2. Procurar livro")
    print("3. Devolver livro")
    print("4. Sair")

    opcao = input("O que deseja fazer?")

    if opcao == "1":
        listar_livros(biblioteca, usuario_logado, usuarios)
    elif opcao == "2":
        procurar_livro(biblioteca, usuario_logado, usuarios)
    elif opcao == "3":  
        devolver_livro(biblioteca, usuario_logado, usuarios)
    elif opcao == "4":
        print("Encerrando...")
        break
    else:
        print("Opção inválida. Tente novamente")
        continue