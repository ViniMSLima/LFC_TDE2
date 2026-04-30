TDE 2 - MÁQUINAS DE ESTADO FINITO E GRAMÁTICAS

Nome: Vinícius Matheus Sary de Lima
Data: 01/05/2026
Link para o arquivo com as soluções: https://github.com/ViniMSLima/LFC_TDE2/Respostas_TDE2.md

--------------------------------------------------------------------------------

QUESTÃO 1

Pergunta:
Faça os diagramas de transição Máquinas de Estados Finitos Determinísticas (MEFD -0, MEFD-1, MEFD-2, MEFD-3, MEFD-4) para reconhecer cada uma das seguintes linguagens a seguir:
a) L_0 = { x | x em {0,1}* e cada 0 em x é seguido por pelo menos um 1 }.
b) L_1 = { x | x em {0,1}* e x termina com 00 }.
c) L_2 = { x | x em {0,1}* e x contém exatamente 3 zeros }.
d) L_3 = { x | x em {0,1}* e x inicia com 1 }.
e) L_4 = { x | x em {0,1}* e x não começa com 1 }.

Resposta:

a) L_0 (MEFD-0)
Estados: q0, q1, q2
Estado Inicial: q0
Estados Finais: q0

Transições:
[INÍCIO] -> q0
q0 --- 1 ---> q0
q0 --- 0 ---> q1
q1 --- 1 ---> q0
q1 --- 0 ---> q2 (morto)
q2 -- 0,1 --> q2

b) L_1 (MEFD-1)
Estados: q0, q1, q2
Estado Inicial: q0
Estados Finais: q2

Transições:
[INÍCIO] -> q0
q0 --- 1 ---> q0
q0 --- 0 ---> q1
q1 --- 1 ---> q0
q1 --- 0 ---> q2
q2 --- 1 ---> q0
q2 --- 0 ---> q2

c) L_2 (MEFD-2)
Estados: q0, q1, q2, q3, q4
Estado Inicial: q0
Estados Finais: q3

Transições:
[INÍCIO] -> q0
q0 --- 1 ---> q0
q0 --- 0 ---> q1
q1 --- 1 ---> q1
q1 --- 0 ---> q2
q2 --- 1 ---> q2
q2 --- 0 ---> q3
q3 --- 1 ---> q3
q3 --- 0 ---> q4 (morto)
q4 -- 0,1 --> q4

d) L_3 (MEFD-3)
Estados: q0, q1, q2
Estado Inicial: q0
Estados Finais: q1

Transições:
[INÍCIO] -> q0
q0 --- 1 ---> q1
q0 --- 0 ---> q2 (morto)
q1 -- 0,1 --> q1
q2 -- 0,1 --> q2

e) L_4 (MEFD-4)
Estados: q0, q1, q2
Estado Inicial: q0
Estados Finais: q0, q1

Transições:
[INÍCIO] -> q0
q0 --- 0 ---> q1
q0 --- 1 ---> q2 (morto)
q1 -- 0,1 --> q1
q2 -- 0,1 --> q2

--------------------------------------------------------------------------------

QUESTÃO 2

Pergunta:
Implemente, utilizando a linguagem C, C++ ou Python um programa capaz de simular cada uma destas máquinas. Observe que a simulação precisa ser da máquina (estados e transições) não de um programa equivalente.

Resposta:
A simulação das máquinas foi desenvolvida em Python. O código completo se encontra no link disponibilizado no cabeçalho deste documento.

Código principal do simulador:

class MEFD:
    def __init__(self, name, states, alphabet, transitions, start_state, accept_states):
        self.name = name
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.start_state = start_state
        self.accept_states = accept_states

    def simulate(self, string):
        current_state = self.start_state
        for char in string:
            if char not in self.alphabet:
                return False
            try:
                current_state = self.transitions[(current_state, char)]
            except KeyError:
                return False
        return current_state in self.accept_states

(O script completo com as definições para as 5 MEFDs está no arquivo simulador_mefd.py)

--------------------------------------------------------------------------------

QUESTÃO 3

Pergunta:
Explique a hierarquia de Chomsky para as gramáticas, destacando as características de cada uma, notadamente no que se refere as limitações impostas a criação de regras de produção. Importante, você precisa explicar a formação das regras de produção para cada uma das gramáticas na hierarquia de Chomsky com exemplos práticos.

Resposta:
A Hierarquia de Chomsky organiza as gramáticas em quatro níveis (Tipos 0 a 3). Cada nível tem regras de produção mais restritas que o anterior.

1. Gramáticas Irrestritas (Tipo 0)
Limitações: Praticamente nenhuma restrição. A regra tem o formato "A -> B", onde "A" e "B" são sequências de variáveis e terminais. O lado esquerdo não pode ser vazio e precisa ter ao menos um não-terminal.
Exemplo: SAB -> baB | B -> b
Autômato: Máquina de Turing.

2. Gramáticas Sensíveis ao Contexto (Tipo 1)
Limitações: O tamanho da cadeia gerada nunca pode ser menor que o da cadeia de origem. O "contexto" ao redor do símbolo deve ser respeitado para a transformação.
Exemplo: aB -> ab | bB -> bb
Autômato: Autômato Linearmente Limitado.

3. Gramáticas Livres de Contexto (Tipo 2)
Limitações: O lado esquerdo da regra deve ser obrigatoriamente um único símbolo não-terminal. A substituição independe do contexto ao redor do símbolo.
Exemplo: S -> aSb | S -> vazio
Autômato: Autômato com Pilha.

4. Gramáticas Regulares (Tipo 3)
Limitações: É a mais restrita. O lado esquerdo deve ser um único não-terminal. O lado direito só pode ter um terminal sozinho ou um terminal seguido de no máximo um não-terminal.
Exemplo: S -> 0A | A -> 1S | A -> 1
Autômato: Máquina de Estados Finitos.

