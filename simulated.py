import random  # randomize state
import copy
import math

ROUNDS_SINCE_CHANGE = 300
ESCAPE_TEMPERATURE = 0.01


# A class representing one of the states
# central is the truth_values_array (ohodnocení)
# truth_values_array[1] = 0    First variable is set to False
# truth_values_array[3] = 1    Third variable is set to True
class CNFState:
    def __init__(self, instance):
        self.truth_values_array = [0] * (instance.number_of_variables + 1)
        self.truth_values_array[0] = -420
        self.of_instance = instance
        self.weight = -1

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
               "Suspect:\t%s\n" % (self.of_instance.id, str(self.truth_values_array), self.weight, self.satisfied, self.suspect_variables_set)

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
        return True

    # Change one bit in state and refresh values
    def flip(self, item_nr):
        return False

    # Randomizes the state completely
    def randomize(self):
        return False

    # Try to find solution with randomize - if not, go with random
    def random_start(self):
        return False

    # Compare two states and decide, which one is better
    def is_better(self, challenger):
        return False

    def random_neighbour(self):
        return False


class KnapsackState:
    def __init__(self, instance):
        self.boxes = instance.current_things
        self.combination_array = [0] * self.boxes  # Initially trivial
        self.state_of_instance = copy.copy(instance)
        self.value = 0
        self.weight = 0

    def is_solution(self):
        if self.weight > self.state_of_instance.original_limit_weight:
            return False
        return True

    def flip(self, item_nr):
        # print("Flip %d" % (item_nr))

        if self.combination_array[item_nr] == 0:
            self.combination_array[item_nr] = 1
            self.value += self.state_of_instance.things_array[item_nr].value
            self.weight += self.state_of_instance.things_array[item_nr].weight
            # print("Item 0 -> 1 ")
            # print("Value: %d\n"
            #      "New V: %d\n"
            #      "Weight: %d\n"
            #      "New:    %d" % (self.value, self.state_of_instance.things_array[item_nr].value,
            #                      self.weight, self.state_of_instance.things_array[item_nr].weight))

        elif self.combination_array[item_nr] == 1:
            self.combination_array[item_nr] = 0
            self.value -= self.state_of_instance.things_array[item_nr].value
            self.weight -= self.state_of_instance.things_array[item_nr].weight
            # print("Item 1 -> 0")
            # print("Value: %d\n"
            #      "New V: %d\n"
            #      "Weight: %d\n"
            #      "New:    %d" % (self.value, self.state_of_instance.things_array[item_nr].value,
            #                      self.weight, self.state_of_instance.things_array[item_nr].weight))
        else:
            print("Could not flip thing in arra. Propably bad limits. Very bad.")

        return

    # Randomizes the state compltely
    def randomize(self):
        # For every thing in array flip a coin
        for thing_nr in range(0, self.boxes):
            if random.randint(0, 1):
                self.flip(thing_nr)

    # Generate random solution
    def random_solution(self):
        for i in range(0, self.boxes * 1000):
            self.randomize()
            if self.is_solution():
                # print("Is a solution. :)")
                return
            # print("Not a solution. :(")

        # I give up, lets go trivial
        self.combination_array = [0] * self.boxes
        self.value = 0
        self.weight = 0
        return

    # For printing the state
    def __str__(self):
        return "--- State of instance nr.%d ---\n" \
               "- Boxes:  %d\n" \
               "- Array:  %s\n" \
               "- Value:  %d\n" \
               "- Weight: %d" % (self.state_of_instance.id, self.boxes, self.combination_array, self.value, self.weight)

    def is_better(self, challanger):
        if not challanger.is_solution():
            return True
        if self.value > challanger.value:
            return True
        return False

    def random_neighbour_solution(self):
        a = list(range(0, self.boxes))
        # print(a)
        random.shuffle(a)
        # print(a)

        original = copy.deepcopy(self)
        # print(original)

        for i in a:
            new = copy.deepcopy(original)
            new.flip(i)
            # print(new)
            # new.flip(random.randint(0, self.boxes-1))
            if new.is_solution():
                # print("Accept as a solution neighbour.")
                return new
            # print("Reject as a solution neighbour.")

        print("Something went terribly bad! This should never happen.\n"
              "Solution has no neighbours which are solutions. WTF?")
        exit(1)


def cool(temperature, a):
    return temperature * a


def equilibrium(state, step, accepted):
    # if accepted >= state.boxes:
    if step >= state.boxes * 2:
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
    coeficient = 100.0 / float(stateA.value)
    diff = 100.0 - (float(stateB.value) * coeficient)
    return diff


def try_state(state, temperature):
    # Zvol náhodného souseda
    new = state.random_neighbour_solution()
    # Přijmi jej, je li lepší
    if new.is_better(state):
        # print("Better")
        return new, True

    # Jinak jej přijmi s převědpodobností závislou na zhoršení
    sigma = float(normalized_value_diff(state, new))
    # print(math.exp(-sigma / temperature))
    if (random.random() < math.exp(-sigma / temperature)):
        # print("Beneveolent")
        return new, True

    # print("Not good enough.")
    return state, False


def solve_sim(self, start_temperature, cooling_coefficient):
    print("-- Simulated Cooling --")

    state = CNFState(self)
    state.random_solution()
    best = CNFState(self)  # Empty state is the default state of CNFState
    temperature = start_temperature
    rounds_without_better_state = 0
    rounds_since_new_state = 0

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

            if state.is_better(best):
                best = copy.deepcopy(state)
                rounds_without_better_state = 0
                accepted += 1
            else:
                rounds_without_better_state += 1
            step += 1

            # print("%d" % (state.value))
            # print("%d" % (best.value))

        temperature = cool(temperature, cooling_coefficient)
        # print("Rounds without new better: %d" % (rounds_without_better_state))

    print("--- Finished ---")
    print(best)
    self.best_cost = best.value
    self.best_solution = best.combination_array

    return best.value
