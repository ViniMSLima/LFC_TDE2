class MEFD:
    def __init__(self, name, states, alphabet, transitions, start_state, accept_states):
        self.name = name
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.start_state = start_state
        self.accept_states = accept_states

    def simulate(self, string):
        print(f"\n--- Simulando {self.name} para a string '{string}' ---")
        current_state = self.start_state
        print(f"Estado inicial: {current_state}")

        for char in string:
            if char not in self.alphabet:
                print(f"Caractere '{char}' não pertence ao alfabeto. Rejeitado.")
                return False

            # Transição: (estado_atual, char) -> próximo_estado
            try:
                next_state = self.transitions[(current_state, char)]
                print(f"Lendo '{char}': transição de {current_state} -> {next_state}")
                current_state = next_state
            except KeyError:
                print(f"Transição indefinida para o estado {current_state} com caractere '{char}'. Rejeitado.")
                return False

        if current_state in self.accept_states:
            print(f"Fim da string. Estado final {current_state} É um estado de aceitação. -> ACEITO")
            return True
        else:
            print(f"Fim da string. Estado final {current_state} NÃO É um estado de aceitação. -> REJEITADO")
            return False

def main():
    alfabeto = {'0', '1'}

    # a) L0 = cada 0 é seguido por pelo menos um 1
    mefd_0 = MEFD(
        name="MEFD-0 (cada 0 seguido por pelo menos um 1)",
        states={'q0', 'q1', 'q2'},
        alphabet=alfabeto,
        start_state='q0',
        accept_states={'q0'},
        transitions={
            ('q0', '1'): 'q0',
            ('q0', '0'): 'q1',
            ('q1', '1'): 'q0',
            ('q1', '0'): 'q2', # erro
            ('q2', '0'): 'q2',
            ('q2', '1'): 'q2',
        }
    )

    # b) L1 = termina com 00
    mefd_1 = MEFD(
        name="MEFD-1 (termina com 00)",
        states={'q0', 'q1', 'q2'},
        alphabet=alfabeto,
        start_state='q0',
        accept_states={'q2'},
        transitions={
            ('q0', '1'): 'q0',
            ('q0', '0'): 'q1',
            ('q1', '1'): 'q0',
            ('q1', '0'): 'q2',
            ('q2', '1'): 'q0',
            ('q2', '0'): 'q2',
        }
    )

    # c) L2 = contém exatamente 3 zeros
    mefd_2 = MEFD(
        name="MEFD-2 (exatamente 3 zeros)",
        states={'q0', 'q1', 'q2', 'q3', 'q4'},
        alphabet=alfabeto,
        start_state='q0',
        accept_states={'q3'},
        transitions={
            ('q0', '1'): 'q0', ('q0', '0'): 'q1',
            ('q1', '1'): 'q1', ('q1', '0'): 'q2',
            ('q2', '1'): 'q2', ('q2', '0'): 'q3',
            ('q3', '1'): 'q3', ('q3', '0'): 'q4',
            ('q4', '1'): 'q4', ('q4', '0'): 'q4', # erro
        }
    )

    # d) L3 = inicia com 1
    mefd_3 = MEFD(
        name="MEFD-3 (inicia com 1)",
        states={'q0', 'q1', 'q2'},
        alphabet=alfabeto,
        start_state='q0',
        accept_states={'q1'},
        transitions={
            ('q0', '1'): 'q1',
            ('q0', '0'): 'q2',
            ('q1', '0'): 'q1', ('q1', '1'): 'q1',
            ('q2', '0'): 'q2', ('q2', '1'): 'q2', # erro
        }
    )

    # e) L4 = não começa com 1
    mefd_4 = MEFD(
        name="MEFD-4 (não começa com 1)",
        states={'q0', 'q1', 'q2'},
        alphabet=alfabeto,
        start_state='q0',
        accept_states={'q0', 'q1'}, # q0 aceita string vazia (não começa com 1)
        transitions={
            ('q0', '0'): 'q1',
            ('q0', '1'): 'q2', # erro
            ('q1', '0'): 'q1', ('q1', '1'): 'q1',
            ('q2', '0'): 'q2', ('q2', '1'): 'q2',
        }
    )

    maquinas = [mefd_0, mefd_1, mefd_2, mefd_3, mefd_4]
    testes = ["", "111", "00", "010111", "10100", "000", "0101010", "1", "0"]

    for mefd in maquinas:
        print(f"\n==========================================")
        print(f"Executando Testes para: {mefd.name}")
        print(f"==========================================")
        for t in testes:
            mefd.simulate(t)

if __name__ == '__main__':
    main()
