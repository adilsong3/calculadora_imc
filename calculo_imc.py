def calculo_imc(peso, altura):
    peso = float(peso)
    altura = float(altura)
    imc = peso / (altura ** 2)

    return round(imc, 2)

def formatar_altura(altura):
    altura = str(altura)
    if len(altura) > 1:
        if float(altura[0]) > 2:
            altura = '0' + altura
        if '.' not in altura[1:]:
            altura = altura[:1] + '.' + altura[1:]
    altura = float(altura)
    return altura

