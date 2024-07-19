# importar bibliotecas necessárias
import PySimpleGUI as sg
from calculo_imc import calculo_imc, formatar_altura

# Criando aparencia da tela
layout = [
    [sg.Text('Calculadora do Indice de Massa Corporal', font=('Helvetica', 14))],
    [sg.Text('Peso (kg) :', size=(8,1), font=('Helvetica', 12)), sg.Input(key='PESO', size=(42,1), tooltip='Exemplo: 95.5')],
    [sg.Text('Altura (m):', size=(8,1), font=('Helvetica', 12)), sg.Input(key='ALTURA', size=(42,1), tooltip='Exemplo: 1.80')],
    [sg.Button('Calcular IMC', size=(42,1), font=('Helvetica', 12))],
    [sg.Text('', size=(30, 1), font=('Helvetica', 14), key='RESULTADO')],
    [sg.Text('', size=(30, 1), font=('Helvetica', 18), key='CATEGORIA')],
]

# Criando a tela
window = sg.Window('Calculadora de IMC', layout, resizable=True)

# loop para executar e manter a tela aberta
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    
    # verificar se o botão foi clicado
    if event == 'Calcular IMC':
        peso = values['PESO']
        altura = values['ALTURA']
        # verificar se o campo peso e altura estão preenchido caso não esteja não permite avançar
        if not peso or not altura:
            sg.popup('Por favor, preencha todos os campos.', title='Aviso')
            continue
        
        # pequena validação de campo peso e altura para saber se digitou numeros
        try:
            peso = float(peso)
            altura = float(altura)
        except ValueError:
            sg.popup('Por favor, digite apenas números nos campos de peso e altura.', title='Aviso')
            continue

        # validação se o que foi digitado em altura está entre 0.3 e 3.0
        if not (0.3 <= altura <= 3.0):
            sg.popup('Por favor, digite um valor de altura válido (entre 0.3 e 3.0 metros).', title='Aviso')
            continue

        ''' 
        formatação final da altura caso permita que o usuário digite numeros inteiros (opcional)
        altura_formatada = formatar_altura(altura)
        imc = calculo_imc(peso, altura_formatada) 
        '''

        # calculo do imc
        imc = calculo_imc(peso, altura)

        # verificar se o imc não está vazio e aplicar as validações por categoria
        if imc is not None:
            window['RESULTADO'].update(f'Seu IMC atual é: {imc}')
            if imc < 17:
                window['CATEGORIA'].update(f'Categoria: Muito abaixo do peso', text_color=f'#{255:02X}{255:02X}{255:02X}')
            elif imc < 18.5:
                window['CATEGORIA'].update(f'Categoria: Abaixo do peso', text_color=f'#{240:02X}{230:02X}{0:02X}')
            elif imc < 24.9: 
                window['CATEGORIA'].update(f'Categoria: Peso normal', text_color=f'#{255:02X}{255:02X}{0:02X}')
            elif imc < 29.9: 
                window['CATEGORIA'].update(f'Categoria: Acima do peso', text_color=f'#{255:02X}{165:02X}{0:02X}')
            elif imc < 34.9: 
                window['CATEGORIA'].update(f'Categoria: Obesidade I', text_color=f'#{255:02X}{140:02X}{0:02X}')
            elif imc < 39.9: 
                window['CATEGORIA'].update(f'Categoria: Obesidade II', text_color=f'#{255:02X}{69:02X}{0:02X}')
            else:
                window['CATEGORIA'].update(f'Categoria: Obesidade III', text_color=f'#{255:02X}{0:02X}{0:02X}')

# fechar janela
window.close()