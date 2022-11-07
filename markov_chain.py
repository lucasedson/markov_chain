#

from numpy.random import rand
from numpy import cumsum
from time import sleep

print("###################################################")
print("\t\t Markov Chain")
print("###################################################\n")

#States
L = [1,2,3,4]


#Probalities Matrix (Transiction Matrix)
S = [[0, 0.6, 0.3, 0.1],
     [0.5, 0, 0.4, 0.1],
     [0.1, 0.4, 0, 0.5],
     [0.1, 0.3, 0.4, 0.2]
     ]



# Choice the State based in Probalities Matrix
def choice_random_state(weights, object):
    cs = cumsum(weights)
    idx = sum(cs < rand())
    return object[idx]

def markov_chain(iter=10):
    def core(S, L, state):
            new_state = state - 1
            new_state = choice_random_state(S[new_state], L)
            return new_state

    state = 1       
    for i in range(0, iter):
        if state == 1: print(i+1,"- Actual State: Run")
        elif state == 2: print(i+1,"- Actual State: Sleep")
        elif state == 3: print(i+1,"- Actual State: Walk")
        elif state == 4: print(i+1,"- Actual State: Eat")

        state = core(S, L, state)
        sleep(1)



if __name__ == "__main__":
    markov_chain(10000)