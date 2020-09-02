import json

# Data to be written


def write_jason(path, alphabet: list, states: list, initial_state: str, accepting_states: list, transitions: list):

    # alphabet = ["a", "b", "c"]
    # states = ["q0", "q1", "q3"]
    # initial_state = "q0"
    # accepting_states = ["q3", "q2"]
    # transitions = [['q0', '0', 'q0'], ['q0', '0', 'q1'], ['q0', '0', 'q2']]

    dictionary = {
        "alphabet": alphabet,
        "states": states,
        "initial_state": initial_state,
        "accepting_states": accepting_states,
        "transitions": transitions
    }

    # Serializing json
    json_object = json.dumps(dictionary, indent=4)

    # Writing to sample.json
    with open("Json&Images/"+path, "w") as outfile:
        outfile.write(json_object)
