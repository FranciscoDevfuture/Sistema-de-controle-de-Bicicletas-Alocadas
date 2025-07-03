# Sistema de Controle de Bicicletas Terminal João Dias
from datetime import datetime

# Lista para armazenar os registros
usuarios = []

# ========================
# Função para carregar registros do arquivo TXT
# ========================
def carregar_de_arquivo_txt():
    try:
        with open('registro_bicicletas.txt', 'r') as arquivo:
            usuario = {}
            for linha in arquivo:
                linha = linha.strip()
                if linha == '---':
                    if usuario:
                        usuarios.append(usuario)
                        usuario = {}
                elif ':' in linha:
                    chave, valor = linha.split(':', 1)
                    usuario[chave.strip()] = valor.strip()
            if usuario:
                usuarios.append(usuario)
        print("📂 Registros carregados do arquivo TXT.\n")
    except FileNotFoundError:
        print("📁 Nenhum arquivo de registros encontrado. Começando com lista vazia.\n")

# ========================
# Função para salvar registros no arquivo TXT
# ========================
def salvar_em_arquivo_txt():
    with open('registro_bicicletas.txt', 'w') as arquivo:
        for usuario in usuarios:
            arquivo.write(f'nome: {usuario["nome"]}\n')
            arquivo.write(f'login: {usuario["login"]}\n')
            arquivo.write(f'vaga: {usuario["vaga"]}\n')
            arquivo.write(f'hora_entrada: {usuario["hora_entrada"]}\n')
            if 'hora_saida' in usuario:
                arquivo.write(f'hora_saida: {usuario["hora_saida"]}\n')
            arquivo.write('---\n')
    print("💾 Registros salvos com sucesso no arquivo 'registro_bicicletas.txt'.\n")

# ========================
# Função para registrar entrada
# ========================
def registrar_entrada():
    nome = input('Digite o nome do usuário: ')
    login = input('Digite o login do usuário: ')
    vaga = input('Digite a vaga onde a bicicleta será estacionada: ')
    hora_entrada = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    usuario = {
        'nome': nome,
        'login': login,
        'vaga': vaga,
        'hora_entrada': hora_entrada
    }

    usuarios.append(usuario)

    print(f'\n✅ Bicicleta registrada com sucesso!')
    print(f'Usuário: {nome}\nLogin: {login}\nVaga: {vaga}\nHora de entrada: {hora_entrada}\n')

# ========================
# Função para registrar saída
# ========================
def registrar_saida():
    login = input('Digite o login do usuário para registrar a saída: ')
    for usuario in usuarios:
        if usuario['login'] == login and 'hora_saida' not in usuario:
            hora_saida = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            usuario['hora_saida'] = hora_saida
            print(f'\n🚲 Bicicleta removida com sucesso!')
            print(f'Usuário: {usuario["nome"]}\nLogin: {usuario["login"]}')
            print(f'Vaga: {usuario["vaga"]}\nHora de entrada: {usuario["hora_entrada"]}')
            print(f'Hora de saída: {hora_saida}\n')
            return
    print("❌ Usuário não encontrado ou bicicleta já retirada.\n")

# ========================
# Função para listar bicicletas estacionadas
# ========================
def listar_bicicletas():
    print("\n📋 Lista de Bicicletas Estacionadas:")
    if not usuarios:
        print("Nenhuma bicicleta registrada.\n")
        return

    encontrou = False
    for usuario in usuarios:
        if 'hora_entrada' in usuario and 'hora_saida' not in usuario:
            encontrou = True
            print(f'Usuário: {usuario["nome"]}')
            print(f'Login: {usuario["login"]}')
            print(f'Vaga: {usuario["vaga"]}')
            print(f'Hora de entrada: {usuario["hora_entrada"]}')
            print('-' * 30)

    if not encontrou:
        print("Nenhuma bicicleta está atualmente estacionada.\n")

# ========================
# Função para exibir o menu
# ========================
def exibir_menu():
    print("===== Sistema de Controle de Bicicletas Versao 1.0 by Franco =====")
    print("1. Registrar Entrada")
    print("2. Registrar Saída")
    print("3. Salvar Registro em Arquivo")
    print("4. Listar Bicicletas Estacionadas")
    print("5. Sair")
    print("=============================================")

# ========================
# Função principal
# ========================
def main():
    carregar_de_arquivo_txt()  # ← carrega registros no início

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        print()

        if opcao == '1':
            registrar_entrada()
        elif opcao == '2':
            registrar_saida()
        elif opcao == '3':
            salvar_em_arquivo_txt()
        elif opcao == '4':
            listar_bicicletas()
        elif opcao == '5':
            salvar_em_arquivo_txt()  # salva antes de sair
            print("👋 Saindo do sistema... Até logo!")
            break
        else:
            print("❗ Opção inválida. Tente novamente.\n")

# Executa o sistema
if __name__ == "__main__":
    main()
