
import random
from datetime import date

# Dados
treinadores = {
    "T1": {"nome": "Aron", "reino": "Valaris", "nivel": "5"},
    "T2": {"nome": "Lyra", "reino": "Eldoria", "nivel": "15"},
    "T3": {"nome": "Jonh Peace", "reino": "Fortune", "nivel": "15"},
    "T4": {"nome": "zynio", "reino": "Godgertown", "nivel": "24"},
    "T5": {"nome": "Luciano Cabral", "reino": "Ifpe", "nivel": "30"},
    "T6": {"nome": "Pablo Espindola", "reino": "Infernal", "nivel": "70"},
    "T7": {"nome": "#$ßɓÿńöð§ïþ", "reino": "desconhecido", "nivel": "666"},


}

dragoes = {
    "D1": {"nome": "Fulgor", "tipo": "fogo", "idade": "50", "poder": "8"},
    "D2": {"nome": "Glacius", "tipo": "gelo", "idade": "80", "poder": "12"},
    "D3": {"nome": "Tralalero", "tipo": "água", "idade": "70", "poder": "25"},
    "D4": {"nome": "Tung Sahur", "tipo": "Madeira", "idade": "140", "poder": "15"},
    "D5": {"nome": "Luana", "tipo": "Fogo", "idade": "17", "poder": "50"},
    "D6": {"nome": "Hidrinius ", "tipo": "água", "idade": "103", "poder": "21"}

}

comida = ["Sim", "Nao"]

data = 1


adocoes = {}

id_treinador_inicial = "T1"

jogador = {
    "xp": 100
}

inimigos = {
    "goblin": {"nome": "Goblin", "nivel": 1, "exp": 10},
    "orc": {"nome": "Orc", "nivel": 3, "exp": 30},
    "orc": {"nome": "Orc", "nivel": 3, "exp": 30},
    "dragao_negro": {"nome": "Dragão Negro", "nivel": 10, "exp": 100},
    "dragao_branco": {"nome": "Dragão Branco dos olhos azuis", "nivel": 50, "exp": 500},
    "caramelo": {"nome": "Cachorro Caramelo", "nivel": 3, "exp": 30},
    "exodia": {"nome": "Exodia", "nivel": 40, "exp": 400},
    "mago_negro": {"nome": "Mago Negro", "nivel": 18, "exp": 180},
    "argentino": {"nome": "Argentino", "nivel": 1, "exp": 10}

}

def escolher_treinador_principal():
    print("\n--- Escolher Treinador Principal ---")

    disponiveis = {tid: t for tid, t in treinadores.items() if t.get("status") == "disponivel"}

    if not disponiveis:
        print("Você ainda não comprou nenhum treinador.")
        return

    for tid, t in disponiveis.items():
        print(f"{tid}: {t['nome']} (Nível {t['nivel']}, Reino: {t['reino']})")

    novo_id = input("Digite o ID do treinador principal desejado: ")
    if novo_id in disponiveis:
        global id_treinador_inicial
        id_treinador_inicial = novo_id
        print(f"Agora você está usando o treinador: {treinadores[novo_id]['nome']}")
    else:
        print("ID inválido ou treinador não foi comprado.")



def menu_principal():
    print(f"\n--- Jornada do Campeão ---")
    print(f"XP disponível: {jogador['xp']}", "--- Dia:", dia, "---")
    if id_treinador_inicial in treinadores:
        t = treinadores[id_treinador_inicial]
        print(f"Seu personagem: {t['nome']} (Nível {t['nivel']}, Reino: {t['reino']})")
    print("1. Gerenciar Treinadores")
    print("2. Gerenciar Dragões")
    print("3. Gerenciar Adoções")
    print("4. Passar Dia e Lutar")
    print("5. Comer e descansar")
    print("6. Trocar treinador principal")

    print("0. Sair")


def menu_crud(entidade):
    print(f"--- {entidade.upper()} ---")
    print("1. Inserir (custa 500 XP)")
    print("2. Alterar (custa 400 XP)")
    print("3. Consultar")
    print("4. Vender (ganha 100 XP)")
    print("0. Voltar")

def comer():
    resultado = random.choice(comida)
    if resultado == "Sim":
        jogador['xp'] += 10
        print("Você conseguiu Comer e se manter Seguro (+10 XP)")
    else:
        jogador['xp'] -= 15
        print("Você foi molestado enquanto descansava")


# definis coisas dos treinadores
def inserir_treinador():
    if jogador['xp'] < 500:
        print("XP insuficiente para comprar um novo treinador.")
        return

    ids_ordenados = sorted(treinadores.keys(), key=lambda x: int(x[1:]))
    for tid in ids_ordenados:
        if treinadores[tid].get("status") != "disponivel":
            proximo_id = tid
            break
    else:
        print("Todos os treinadores já foram comprados.")
        return

    treinador = treinadores[proximo_id]
    treinador["status"] = "disponivel"
    jogador['xp'] -= 500
    print(f"Você comprou o treinador {treinador['nome']} (ID: {proximo_id})! (-500 XP)")


def alterar_treinador():
    if jogador['xp'] < 400:
        print("XP insuficiente para alterar treinador.")
        return
    id = input("ID do Treinador para alterar: ")
    if id in treinadores:
        nome = input("Novo nome: ")
        reino = input("Novo reino: ")
        nivel = input("Novo nível: ")
        treinadores[id] = {"nome": nome, "reino": reino, "nivel": nivel}
        jogador['xp'] -= 400
        if int(nivel) > 30:
            print("Você não é Deus pra criar um personagem tão OP")
        else:
            print("Treinador alterado! (-400 XP)")
    else:
        print("Treinador não encontrado.")

def consultar_treinadores():
    for id, dados in treinadores.items():
        print(f"{id}: {dados}")

def vender_treinador():
    id = input("ID do Treinador para vender: ")
    if id in treinadores:
        del treinadores[id]
        jogador['xp'] += 100
        print("Treinador vendido! (+100 XP)")
    else:
        print("Treinador não encontrado.")

# dwfinir coisas dos dragões
def inserir_dragao():
    if jogador['xp'] < 500:
        print("XP insuficiente para inserir dragão.")
        return
    id = input("ID do Dragão: ")
    nome = input("Nome: ")
    tipo = input("Tipo (fogo, gelo, etc.): ")
    idade = input("Idade: ")
    poder = input("Nível de poder (1-30): ")
    dragoes[id] = {"nome": nome, "tipo": tipo, "idade": idade, "poder": poder}
    jogador['xp'] -= 500
    if int(poder) > 30:
        print("Você não é Deus pra criar um personagem tão OP")
    else:
        print("Dragão cadastrado! (-500 XP)")

def alterar_dragao():
    if jogador['xp'] < 400:
        print("XP insuficiente para alterar dragão.")
        return
    id = input("ID do Dragão para alterar: ")
    if id in dragoes:
        nome = input("Novo nome: ")
        tipo = input("Novo tipo: ")
        idade = input("Nova idade: ")
        poder = input("Novo nível de poder: ")
        dragoes[id] = {"nome": nome, "tipo": tipo, "idade": idade, "poder": poder}
        jogador['xp'] -= 400
        if int(poder) > 30:
            print("Você não é Deus pra criar um personagem tão OP")
        else:
            print("Dragão alterado! (-400 XP)")
    else:
        print("Dragão não encontrado.")

def consultar_dragoes():
    for id, dados in dragoes.items():
        print(f"{id}: {dados}")

def vender_dragao():
    id = input("ID do Dragão para vender: ")
    if id in dragoes:
        del dragoes[id]
        jogador['xp'] += 100
        print("Dragão vendido! (+100 XP)")
    else:
        print("Dragão não encontrado.")

# definir coisas das adoções
def registrar_adocao():
    if jogador['xp'] < 500:
        print("XP insuficiente para adotar um dragão.")
        return
    id = input("ID da adoção: ")
    id_treinador = input("ID do Treinador: ")
    id_dragao = input("ID do Dragão: ")
    data = date.today().strftime("%d/%m/%Y")

    if id_treinador not in treinadores or id_dragao not in dragoes:
        print("Treinador ou dragão inválido.")
        return

    nivel_treinador = int(treinadores[id_treinador]["nivel"])
    poder_dragao = int(dragoes[id_dragao]["poder"])

    if nivel_treinador <= poder_dragao:
        print("Adoção não permitida: o nível do treinador deve ser maior que o nível de poder do dragão.")
        return
    jogador['xp'] -= 500

    adocoes[id] = {"treinador": id_treinador, "dragao": id_dragao, "data": data, "status": "ativo"}
    print("Adoção registrada! (-500 XP)")

def consultar_dragoes():
    for id, dados in dragoes.items():
        print(f"{id}: {dados}")

def vender_dragao():
    id = input("ID do Dragão para vender: ")
    if id in dragoes:
        del dragoes[id]
        jogador['xp'] += 100
        print("Dragão vendido! (+100 XP)")
    else:
        print("Dragão não encontrado.")

# definir coisas das adoções
def registrar_adocao():
    if jogador['xp'] < 500:
        print("XP insuficiente para adotar um dragão.")
        return
    id = input("ID da adoção: ")
    id_treinador = input("ID do Treinador: ")
    id_dragao = input("ID do Dragão: ")

    if id_treinador not in treinadores or id_dragao not in dragoes:
        print("Treinador ou dragão inválido.")
        return

    nivel_treinador = int(treinadores[id_treinador]["nivel"])
    poder_dragao = int(dragoes[id_dragao]["poder"])

    if nivel_treinador <= poder_dragao:
        print("Adoção não permitida: o nível do treinador deve ser maior que o nível de poder do dragão.")
        return
    jogador['xp'] -= 500

    adocoes[id] = {"treinador": id_treinador, "dragao": id_dragao, "data": data, "status": "ativo"}
    print("Adoção registrada! (-500 XP)")

def consultar_adocoes():
    for id, dados in adocoes.items():
        print(f"{id}: {dados}")

def cancelar_adocao():
    id = input("ID da adoção para cancelar: ")
    if id in adocoes:
        adocoes[id]["status"] = "cancelado"
        print("Adoção cancelada.")
    else:
        print("Adoção não encontrada.")

# lutas

def passar_dia():
    global dia
    print("\n--- PASSAR DIA ---")

    if id_treinador_inicial not in treinadores:
        print("Treinador inicial não encontrado.")
        return

    treinador = treinadores[id_treinador_inicial]
    print(f"\nSeu treinador {treinador['nome']} (Nível {treinador['nivel']}) está enfrentando um inimigo...")

    inimigo = random.choice(list(inimigos.values()))
    print(f"Enfrentou: {inimigo['nome']} (Nível {inimigo['nivel']})")

    if int(treinador['nivel']) >= inimigo['nivel']:
        print(f"Vitória! Ganhou {inimigo['exp']} de experiência.")
        novo_nivel = int(treinador['nivel']) + inimigo['exp'] // 10
        if novo_nivel > 100:
            novo_nivel = 100
        treinador['nivel'] = str(novo_nivel)
        jogador['xp'] += inimigo['exp']
        print(f"Ganhou {inimigo['exp']} XP!")
    else:
        print("Derrota. Nenhuma experiência ganha.")

    dia += 1


# loop principal
while True:
    menu_principal()
    op = input("Escolha uma opção: ")

    if op == "1":
        while True:
            menu_crud("Treinador")
            acao = input("Escolha: ")
            if acao == "1":
                inserir_treinador()
            elif acao == "2":
                alterar_treinador()
            elif acao == "3":
                consultar_treinadores()
            elif acao == "4":
                vender_treinador()
            elif acao == "0":
                break
            else:
                print("Opção inválida.")

    elif op == "2":
        while True:
            menu_crud("Dragão")
            acao = input("Escolha: ")
            if acao == "1":
                inserir_dragao()
            elif acao == "2":
                alterar_dragao()
            elif acao == "3":
                consultar_dragoes()
            elif acao == "4":
                vender_dragao()
            elif acao == "0":
                break
            else:
                print("Opção inválida.")

    elif op == "3":
        while True:
            print("\n--- ADOÇÕES ---")
            print("1. Registrar adoção")
            print("2. Consultar adoções")
            print("3. Cancelar adoção")
            print("0. Voltar")
            acao = input("Escolha: ")
            if acao == "1":
                registrar_adocao()
            elif acao == "2":
                consultar_adocoes()
            elif acao == "3":
                cancelar_adocao()
            elif acao == "0":
                break
            else:
                print("Opção inválida")

    elif op == "4":
        passar_dia()
    elif op == "5":
        comer()
    elif op == "6":
        escolher_treinador_principal()

    elif op == "0":
        print("Saindo... Até logo!")
        break
    else:
        print("Opção inválida")