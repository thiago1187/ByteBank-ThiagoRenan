# ByteBank v2

## Integrantes

- Thiago Alves

## Descricao

O ByteBank e um sistema bancario de linha de comando escrito em Python puro, sem
bibliotecas externas. Ele roda no terminal e permite cadastrar varias contas, cada
uma com nome do titular, chave pix, saldo, historico de transacoes e fila de boletos.

O programa foi construido em tres niveis. No nivel 1 existe apenas um saldo e as
operacoes basicas de deposito e saque, com validacao de valor negativo, valor invalido
e saldo insuficiente. No nivel 2 entra a lista de contas: e possivel cadastrar contas
diferentes, acessar uma delas pelo numero e transferir dinheiro entre elas por PIX,
usando a chave pix como identificador do destino. No nivel 3 cada conta ganha um
extrato e uma fila de boletos.

Na v2 o codigo foi separado em arquivos por assunto, cada um com funcoes pequenas:

- `main.py` - os menus e a execucao do programa
- `banco.py` - a lista de contas, o cadastro, a busca por chave ou numero e o extrato
- `entrada.py` - a leitura e validacao dos valores digitados
- `operacoes.py` - deposito, saque, pix, extrato e estorno
- `boletos.py` - a fila de boletos
- `relatorio.py` - a soma dos gastos por categoria
- `pontos.py` - os BytePoints e o cashback
- `cofrinhos.py` - as caixinhas de investimento
- `credito.py` - o cartao de credito e a fatura
- `moedas.py` - a carteira de moedas estrangeiras
- `emprestimos.py` - o emprestimo pre-aprovado e as parcelas

## Funcionalidades

### Nivel 1
- Consultar saldo
- Depositar
- Sacar
- Validacao de valor menor ou igual a zero, valor nao numerico e saldo insuficiente

### Nivel 2
- Cadastrar conta (recusa nome ou chave em branco e chave pix repetida)
- Acessar conta pelo numero
- PIX entre contas (recusa chave inexistente e transferencia para a propria conta)

### Nivel 2 intermediario (v2)
- Categoria obrigatoria no saque, no pix e no boleto (Alimentacao, Transporte, Lazer,
  Contas e Outros)
- Relatorio de gastos por categoria, com o valor e o percentual de cada uma
- BytePoints: 1 ponto a cada R$ 10,00 em saques e transferencias
- Resgate de cashback em multiplos de 100 pontos (100 pontos = R$ 5,00)
- Caixinhas de investimento: criar com um objetivo, guardar, resgatar e simular o
  rendimento de 0,5% no mes
- Cartao de credito: comprar dentro do limite disponivel, ver a fatura com as compras e
  pagar a fatura com o saldo da conta, restabelecendo o limite
- Carteira multimoedas: comprar e vender USD, EUR e BTC por taxas fixas
- Emprestimo pre-aprovado de ate 3x o saldo, com simulacao de juros simples de 2% ao
  mes, contratacao parcelada e pagamento de parcela

### Nivel 3
- Extrato com todas as transacoes da conta
- Estorno da ultima transacao
- Agendar boletos
- Ver a fila de boletos
- Liquidar pagamentos na ordem de agendamento

## Pilha e fila

O **extrato** e uma pilha (LIFO). Cada deposito, saque, PIX ou boleto pago entra no
topo com `append`, e o estorno sempre desfaz a ultima transacao com `pop()` — a
ultima que entrou e a primeira que sai.

A **fila de boletos** e uma fila (FIFO). Um boleto agendado entra no fim da lista com
`append`, e a liquidacao paga sempre o primeiro da fila com `pop(0)` — o primeiro que
entrou e o primeiro que sai. Se um boleto nao couber no saldo, a liquidacao para nele
e os seguintes continuam agendados.

## Como executar

```
python3 main.py
```
