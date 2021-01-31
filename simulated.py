import random  # randomize state
import copy
import math

ROUNDS_SINCE_CHANGE = 5000
ESCAPE_TEMPERATURE = 0.001
REWARD = 1.5


# A class representing one of the states
# central is the truth_values_array (ohodnocení)
# truth_values_array[1] = 0    First variable is set to False
# truth_values_array[3] = 1    Third variable is set to True
class CNFState:
    def __init__(self, instance):
        self.variables = instance.number_of_variables
        self.truth_values_array = [0] * (self.variables + 1)
        self.truth_values_array[0] = -420
        self.of_instance = instance
        self.weight = -1
        self.orig_weight = -1

        self.satisfied = False
        self.suspect_variables_set = set()

        # Refresh instance
        self.refresh()

    # Prints the state
    def __str__(self):
        return "--- State of instance nr %d ---\n" \
               "TVA:\t\t%s\n" \
               "Weight:\t\t%d\n" \
               "Satisfied:\t%r\n" \
               "Suspect:\t%s\n" % (self.of_instance.id, str(self.truth_values_array), self.weight, self.satisfied,
                                   self.suspect_variables_set)

    # Returns True if this CNF configuration state has all maxterms satisfied
    # Sets the "satisfied" attribute
    # Creates up-to date suspect variables set
    def is_solution(self):
        self.satisfied = True
        # For every maxterm find out if it is satisfied
        for maxterm in self.of_instance.maxterm_array:
            if not maxterm.isSatisfiedWith(self.truth_values_array):
                # If not get its variables and add them to "suspect_variables_set" ans set "is_satisfied" to False
                self.suspect_variables_set = self.suspect_variables_set.union(maxterm.getVars())
                self.satisfied = False

        return self.satisfied

    # Sets the "satisfied" and "suspect_variables_set" attributes with is_solution method
    # Calculates the current weight to "weight" attribute
    def refresh(self):
        self.is_solution()
        current_weight = 0
        j = -1
        # For every variable that is set as True, find the weight.
        for variable in self.truth_values_array:
            j += 1
            if (variable == 0) or (variable == -420):
                continue
            elif variable == 1:
                current_weight += self.of_instance.weight_of_variables[j]
            else:
                print("Unexpected variable weight when refreshing.")
        self.weight = current_weight
        self.orig_weight = self.weight  # save weight before multiplication for printing

        # Multiply price by REWARD if state is satisfied
        if self.satisfied:
            self.weight = self.weight * REWARD

        return True

    # Change one bit in state and refresh values
    def flip(self, item_nr):
        if item_nr > self.variables:
            print("Index out of rangle when flipping. Very bad!")
        elif self.truth_values_array[item_nr] == 1:
            self.truth_values_array[item_nr] = 0
        elif self.truth_values_array[item_nr] == 0:
            self.truth_values_array[item_nr] = 1
        else:
            print("Unexpected value in truth values array.")
        self.refresh()
        return False

    # Randomizes the state completely
    def randomize(self):
        # For every thing in array flip a coin
        for thing_nr in range(1, self.variables + 1):
            if random.randint(0, 1):
                self.flip(thing_nr)
        return False

    # Try to find solution with randomize - if not, go with random
    def random_start(self):
        for i in range(0, self.variables * 1000):
            self.randomize()
            if self.is_solution():
                # print("Is a solution. :)")
                return True
            # print("Not a solution. :(")

        self.randomize()
        return False

    # Compare two states and decide, which one is better
    def is_better(self, challenger):
        # Only compare weights (reward is given in refresh)
        return self.weight >= challenger.weight

        # -- First implemetation, now obsolete --
        # if (challenger.satisfied and self.satisfied):
        #     return self.weight >= challenger.weight  # Better is the one with bigger weight
        # # -- None are solution
        # elif ((not challenger.satisfied) and (not self.satisfied)):
        #     return self.weight >= challenger.weight  # Better is the one with bigger weight
        # # -- Only this one is solution
        # elif ((not challenger.satisfied) and self.satisfied):
        #     return True  # Yes, this one is_better than challenger
        # # -- Only challenger is solution
        # elif (challenger.satisfied and (not self.satisfied)):
        #     return False  # No, this one is NOT better than challenger
        # return False

    def random_neighbour(self):
        new = copy.deepcopy(self)

        # Always pick random! (NEW implemetation)
        to_flip = random.randrange(1, self.variables + 1)
        # print("Flipping %d" % to_flip)
        new.flip(to_flip)

        # -- First implemetation (change only variables in unsatisfied maxterms)
        # If it is satisfied flip any random variable
        # if self.satisfied:
        #     to_flip = random.randrange(1, self.variables + 1)
        #     new.flip(to_flip)
        # # If it is not satisfied flip any variable from suspect_variables_set (variables in unsolved maxterms)
        # else:
        #     # Convert set to list because od python set implementation
        #     suspect_list = list(self.suspect_variables_set)
        #     random.shuffle(suspect_list)
        #     random_suspect_var = suspect_list.pop()
        #     new.flip(random_suspect_var)

        return new


def cool(temperature, a):
    return temperature * a


def equilibrium(state, step, accepted):
    # if accepted >= state.boxes:
    if step >= state.variables * 2:
        return True
    return False


def frozen(t, rounds_without_better_state, rounds_since_new_state):
    # print(rounds_since_new_state)
    # The state did not change for too long
    if rounds_since_new_state > ROUNDS_SINCE_CHANGE:
        return True

    # Hardcoded temperature
    if t < ESCAPE_TEMPERATURE:
        print("Escaping wierd loop in constantly better states")
        return True

    return False


def normalized_value_diff(stateA, stateB):
    coeficient = 100.0 / float(stateA.weight)
    diff = 100.0 - (float(stateB.weight) * coeficient)
    return diff


def try_state(state, temperature):
    # Zvol náhodného souseda
    new = state.random_neighbour()
    # Přijmi jej, je li lepší
    # print("New (%d %r) is better than state (%d %r)" % (new.weight, new.satisfied, state.weight, state.satisfied))
    if new.is_better(state):
        # print("Better")
        return new, True

    # Jinak jej přijmi s převědpodobností závislou na zhoršení
    sigma = float(normalized_value_diff(state, new))
    if (random.random() < math.exp(-sigma / temperature)):
        # print("Beneveolent")
        return new, True

    # print("Not good enough.")
    return state, False


def solve_sim(self, start_temperature, cooling_coefficient, output_chart_data_filename):
    print("-- Simulated Cooling --")

    state = CNFState(self)
    state.random_start()
    print("-- End of start --")
    best = CNFState(self)  # Empty state is the default state of CNFState
    temperature = start_temperature
    rounds_without_better_state = 0
    rounds_since_new_state = 0
    # For automatic chart data saving
    f = open(output_chart_data_filename, "w")

    while not frozen(temperature, rounds_without_better_state, rounds_since_new_state):
        # print("New temp is %d" % (temperature))
        step = 0
        accepted = 0

        while not equilibrium(state, step, accepted):
            state, n = try_state(state, temperature)
            if n == True:
                rounds_since_new_state = 0
            else:
                rounds_since_new_state += 1

            # if state.is_better(best):
            if state.is_better(best) and state.satisfied:
                best = copy.deepcopy(state)
                rounds_without_better_state = 0
                accepted += 1
            else:
                rounds_without_better_state += 1
            step += 1

            # Save evolution of weight for graphing purposes
            # print("%d" % (best.weight))
            # print("%d" % (state.weight))
            # f.write("%d\n" % (state.weight))
            f.write("%d\n" % (state.orig_weight))

        temperature = cool(temperature, cooling_coefficient)

    f.close()
    print("--- Finished ---")
    print(best)
    # self.best_weight = best.weight
    self.best_weight = best.orig_weight
    self.best_solution = best.truth_values_array
    self.solved = True

    # return best.weight
    return best.orig_weight
