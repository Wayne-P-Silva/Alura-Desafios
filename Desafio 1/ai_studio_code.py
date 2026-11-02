def somar(a: float, b: float) -> float:
    """Retorna a soma de dois números."""
    return a + b


def subtrair(a: float, b: float) -> float:
    """Retorna a subtração do primeiro número pelo segundo."""
    return a - b


def multiplicar(a: float, b: float) -> float:
    """Retorna o produto de dois números."""
    return a * b


def dividir(a: float, b: float) -> float:
    """Retorna a divisão do numerador pelo denominador.

    Lança ZeroDivisionError caso o denominador seja zero.
    """
    if b == 0:
        raise ZeroDivisionError('Não é possível realizar divisão por zero.')
    return a / b


def obter_numero(mensagem: str) -> float:
    """Garante que a entrada do usuário seja convertida em um número válido."""
    while True:
        entrada = input(mensagem).strip().replace(',', '.')
        try:
            return float(entrada)
        except ValueError:
            print('Erro: Por favor, digite um número válido (ex: 10 ou 3.5).')


def exibir_menu() -> None:
    """Exibe as opções disponíveis para o usuário."""
    print('\n' + '=' * 30)
    print('      CALCULADORA EM PYTHON')
    print('=' * 30)
    print('1 - Adição (+)')
    print('2 - Subtração (-)')
    print('3 - Multiplicação (*)')
    print('4 - Divisão (/)')
    print('0 - Sair')
    print('=' * 30)


def calculadora() -> None:
    """Função principal que orquestra a execução da calculadora."""
    operacoes = {
        '1': ('Adição', '+', somar),
        '2': ('Subtração', '-', subtrair),
        '3': ('Multiplicação', '*', multiplicar),
        '4': ('Divisão', '/', dividir),
    }

    while True:
        exibir_menu()
        opcao = input('Escolha uma opção (0 a 4): ').strip()

        if opcao == '0':
            print('\nEncerrando a calculadora. Até mais!')
            break

        if opcao not in operacoes:
            print(
                '\nOpção inválida! Por favor, escolha um número entre 0 e 4.'
            )
            continue

        nome_op, simbolo, funcao_calculo = operacoes[opcao]
        print(f'\n--- Operação Selecionada: {nome_op} ---')

        num1 = obter_numero('Digite o primeiro número: ')
        num2 = obter_numero('Digite o segundo número: ')

        try:
            resultado = funcao_calculo(num1, num2)
            # Formatação limpa: exibe como inteiro se não tiver decimais
            res_formatado = (
                f'{resultado:.2f}' if resultado % 1 != 0 else f'{int(resultado)}'
            )
            print(f'\nResultado: {num1} {simbolo} {num2} = {res_formatado}')
        except ZeroDivisionError as erro:
            print(f'\nErro matemático: {erro}')


if __name__ == '__main__':
    calculadora()