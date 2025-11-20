import string
from automata.fa.dfa import DFA
from visual_automata.fa.dfa import VisualDFA
from automata.base.exceptions import InvalidSymbolError

lowercase_letters = set(string.ascii_lowercase)
uppercase_letters = set(string.ascii_uppercase)

all_letters = lowercase_letters.union(uppercase_letters)

states = {"q0", "q1", "q_dead"}
# The initial state is 'q0'.
initial_state = "q0"
# 'q1' is the only accepting state.
final_states = {"q1"}

transitions = {
    'q0': {char: 'q1' for char in all_letters},
    'q1': {
        **{char: 'q1' for char in lowercase_letters},
        **{char: 'q_dead' for char in uppercase_letters}
    },
    'q_dead': {char: 'q_dead' for char in all_letters}
}


dfa = VisualDFA(
    states=states,
    input_symbols=all_letters,
    transitions=transitions,
    initial_state=initial_state,
    final_states=final_states,
)

# --- Visualize the new DFA ---
print("Generating updated DFA diagram...")
# dfa.show_diagram(filename="updated_word_dfa")
print("Diagram saved to 'updated_word_dfa.png'")
print("-" * 30)


# -- Create a function to test strings (this function does not need changes) ---

def check_word(input_string: str):
    """
    Checks if a string is accepted by the DFA and prints the result.
    Handles invalid symbols by treating them as a rejection.
    """
    try:
        if dfa.accepts_input(input_string):
            print("Accepted")
        else:
            print("Not Accepted")
    except InvalidSymbolError:
        print("Not Accepted")


if __name__ == "__main__":
    test_cases = [
        "word",          
        "a",             
        "Word",         
        "Another",      
        "A",             
        "wOrd",      
        "WORD",          
        "",             
        "word1",       
        "w-o-r-d",    
        "1word"       
    ]

    print("Testing strings against the updated DFA:")
    for test in test_cases:
        print(f'Input: "{test}" -> ', end="")
        check_word(test)