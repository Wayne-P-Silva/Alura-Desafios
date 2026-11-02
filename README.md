# Alura-Desafios, Desafio 1
Pronpt: 
Preciso que você como agente de dados gere uma calculadora em Python com as quatro operações básicas (adição, subtração, multiplicação e divisão) e me explique como a aplicação funciona, após isso, responda para mim as seguintes questões:
Quais são os principais componentes do código gerado?
Como a aplicação recebe os números e identifica a operação escolhida?
Como a lógica de programação é utilizada para realizar os cálculos e apresentar os resultados?

reposta em código na pasta indicada:

- Retorno das questões e como funciona a aplicação >

Como a aplicação funciona
Inicialização: Ao executar o programa, a função calculadora() inicia um laço contínuo (while True) que exibe um menu com as opções de 1 a 4 para operações e 0 para sair.
Seleção: O usuário escolhe a operação desejada digitando o dígito correspondente.
Coleta e Validação: A aplicação solicita o primeiro e o segundo número. A função auxiliar obter_numero trata pontuação (converte vírgula para ponto) e impede travamentos caso o usuário digite texto ou letras acidentalmente.
Processamento: O programa chama a função aritmética correspondente à operação escolhida.
Apresentação e Continuidade: O cálculo é feito, o resultado é exibido na tela formatado e o menu reaparece, permitindo novos cálculos até que a pessoa decida sair digitando 0.
Respostas às Questões
1. Quais são os principais componentes do código gerado?
O código é dividido em quatro blocos essenciais da engenharia de software:
Funções Aritméticas Especializadas (somar, subtrair, multiplicar, dividir): Cada uma possui responsabilidade única (Single Responsibility Principle), recebendo dois parâmetros numéricos e devolvendo o resultado correspondente.
Componente de Entrada e Validação (obter_numero): Uma camada de blindagem (sanitização) que garante que o programa só prossiga quando o usuário fornecer valores numéricos reais, tratando exceções de conversão (ValueError).
Componente de Interface / Menu (exibir_menu): Responsável pela apresentação visual no console, facilitando a interação e legibilidade.
Orquestrador Central (calculadora): O laço de controle que integra o menu, mapeia as escolhas do usuário usando uma estrutura de dicionário (dict), invoca o cálculo correto e gere o ciclo de vida do programa (iniciar, repetir e encerrar).
2. Como a aplicação recebe os números e identifica a operação escolhida?
Identificação da Operação:
O comando input() captura a opção do usuário como texto (string).
O método .strip() elimina espaços vazios acidentais.
Em vez de longas cadeias repetitivas de if/elif, o código utiliza um dicionário de despacho (operacoes). A chave digitada (ex: '1', '2') é validada com o operador in operacoes. Caso exista, o programa desempacota o nome da operação, o símbolo e o ponteiro para a função correspondente.
Recepção e Tratamento dos Números:
A função obter_numero() utiliza input() para capturar o dado bruto.
Realiza o pré-processamento com .replace(',', '.'), permitindo tanto o padrão brasileiro (ex: 7,5) quanto o internacional (ex: 7.5).
Tenta converter para ponto flutuante (float(entrada)). Se a conversão for bem-sucedida, o número é retornado. Se falhar, o bloco try/except captura o ValueError e repete a pergunta sem interromper o sistema.
3. Como a lógica de programação é utilizada para realizar os cálculos e apresentar os resultados?
A lógica se apoia nos seguintes pilares fundamentais da programação:
Estrutura de Repetição (while True): Mantém a aplicação viva e receptiva a múltiplos comandos sucessivos, evitando que o programa encerre abruptamente após uma única conta.
Controle de Fluxo Condicional (if, break, continue):
Se a opção for '0', o comando break interrompe o laço e finaliza o script.
Se a opção for inexistente, o continue reinicia o ciclo com uma mensagem de alerta.
Tratamento de Exceções (try / except): A divisão implementa uma verificação lógica explícita (if b == 0), disparando um ZeroDivisionError. O orquestrador captura esse erro com elegância, informando ao usuário o motivo da impossibilidade sem quebrar o programa (crash).
Funções de Primeira Classe (Higher-Order Functions / Callables): No Python, funções podem ser guardadas em estruturas de dados. Ao selecionar a opção, a variável funcao_calculo recebe a própria função (somar, dividir, etc.) e a executa dinamicamente como funcao_calculo(num1, num2).
Formatação e Apresentação: Utiliza f-strings combinadas com o operador módulo (resultado % 1 != 0) para verificar se o número tem casas decimais úteis, exibindo inteiros de forma limpa (ex: 10 em vez de 10.00) e dízimas/reais com duas casas decimais (ex: 3.33).
