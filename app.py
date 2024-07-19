'''
○ Criar uma janela principal.
○ Adicionar campos de entrada para o peso (em kg) e altura (em metros(exemplo:
1.70, 1.80)
○ Adicionar um botão para calcular o IMC.
○ Adicionar um campo para exibir o resultado do IMC.
○ Adicionar um campo para exibir a categoria do IMC
i. Muito abaixo do peso
ii. Abaixo do peso
iii. Peso normal
iv. Acima do peso
v. Obesidade I
vi. Obesidade II
vii. Obesidade III
○ Personalize as cores da categoria para que tudo fique mais intuitivo(coloque
cores diferentes para cada nível
i. (ex:vá de branco para vermelho, de acordo com o nível de obesidade)
'''

import PySimpleGUI as sg
from calculo_imc import calculo_imc, formatar_altura

layout = [
    [sg.Text('Calculadora do Indice de Massa Corporal', font=('Helvetica', 14))],
    [sg.Text('Peso (kg) :', size=(8,1), font=('Helvetica', 12)), sg.Input(key='PESO', size=(42,1), tooltip='Exemplo: 95.5')],
    [sg.Text('Altura (m):', size=(8,1), font=('Helvetica', 12)), sg.Input(key='ALTURA', size=(42,1), tooltip='Exemplo: 1.80')],
    [sg.Button('Calcular IMC', size=(42,1), font=('Helvetica', 12))],
    [sg.Text('', size=(30, 1), font=('Helvetica', 14), key='RESULTADO')],
    [sg.Text('', size=(30, 1), font=('Helvetica', 18), key='CATEGORIA')],
]

window = sg.Window('Calculadora de IMC', layout, resizable=True)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    if event == 'Calcular IMC':
        peso = values['PESO']
        altura = values['ALTURA']
        if not peso or not altura:
            sg.popup('Por favor, preencha todos os campos.', title='Aviso')
            continue
        try:
            peso = float(peso)
        except ValueError:
            sg.popup('Por favor, digite apenas números nos campos de peso e altura.', title='Aviso')
            continue

        if not (0.3 <= float(altura) <= 3.0):
            sg.popup('Por favor, digite um valor de altura válido (entre 0.3 e 3.0 metros).', title='Aviso')
            continue

        altura_formatada = formatar_altura(altura)
        imc = calculo_imc(peso, altura_formatada)
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

window.close()