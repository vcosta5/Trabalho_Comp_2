import PySimpleGUI as sg         # chamar o pysimple com "sg"

layout = [
    [sg.Text("Bem Vindo ao Fórum dos Tim Maias!")],
    [sg.Text("Usuário: ")], [sg.InputText(key='-NAME-')],
    [sg.Text("Senha: ")], [sg.InputText(key="-PASSWORD-")],
    [sg.Button("Entrar"), sg.Button("Novo Usuário"), sg.Button("Sair")],
    [sg.Text("")],
]

janela = sg.Window("Título do fórum aqui",layout, size=(300,170), element_justification='center')

while True:
    evento, valores = janela.read()    #evento = todos os clicks do usuário | valores = info dos usuários
    if evento == sg.WIN_CLOSED or evento == "Sair":
        break
    if evento == "Entrar":
        print("etc etc")

    if evento == "Novo Usuário":    # aqui começa o link com persistÊncia de dados
        print("cadastrando")    #apagar essa linha depois
janela.close()