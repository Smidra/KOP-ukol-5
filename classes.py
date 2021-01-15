import simulated


# Represents one instance of a thing used in a Knapsack problem
class Thing:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.ratio = value / weight
        self.sequence = -1

    # For print(item1) usage
    def __str__(self):
        return "--- Item ---\n" \
               "- Weight: %d\n" \
               "- Value:  %d\n" \
               "- Ratio:  %f" % (self.weight, self.value, self.ratio)

    # For listing things inside instance
    def __repr__(self):
        # return "%d/%d/%f" % (self.weight, self.value, self.ratio)
        return "%d/%d" % (self.weight, self.value)


# Represents one instance of a Knapsack problem
class KnapsackInstance:
    def __init__(self, id, expecting_things, limit_weight, min_cost):
        self.id = id
        self.expecting_things = expecting_things
        self.limit_weight = limit_weight
        self.original_limit_weight = limit_weight
        self.min_cost = min_cost
        self.current_things = 0
        self.complexity = -1
        self.complexity_brute = -1
        self.time = -1
        self.things_array = []
        self.best_cost = -1
        self.best_solution = []
        self.best_acceptable_cost = -1
        self.best_acceptable_solution = []
        self.value_of_all = 0

        self.decompose_array = []
        self.decompose_builder = []

        self.best_cost_reduced = -1

    # Appends one more thing to the array of things in this knapsack problem
    def add_thing(self, thing):
        self.things_array.append(thing)
        self.things_array[-1].sequence = self.current_things
        self.current_things += 1
        self.value_of_all = self.value_of_all + thing.value

    # For printing the instance
    def __str__(self):
        return "=== Knapsack instance nr.%d ===\n" \
               "- Limit weight:  %d\n" \
               "- Nr. of things: %d\n" \
               "- Minimal cost:  %d\n" \
               "- Best cost:    %d\n" \
               "- Best solution:%s\n" \
               "- Complexity:   %d\n" \
               "- Brute force:  %d\n" \
               "- Time:         %f\n" \
               "- Things: %s" % (
                   self.id, self.limit_weight, self.current_things, self.min_cost, self.best_cost, self.best_solution,
                   self.complexity, self.complexity_brute, self.time, self.things_array)

    # For printing the decompose array
    def print_decompose(self):
        for word in self.decompose_array:
            print(word)
        return

    # # Brute force without cutting
    # solve_brute = brute_force.solve_brute
    # brute = brute_force.brute
    #
    # # Solve the instance brute force with cutting
    # solve_brute_cut = brute_force_cut.solve_brute_cut
    # brute_cut = brute_force_cut.brute_cut
    #
    # # Solve the instance with branch and bound cutting (weight+cost)
    # solve_branch_and_bound = branch_and_bound.solve_branch_and_bound
    # branch_and_bound = branch_and_bound.branch_and_bound
    #
    # # Greedy
    # solve_greedy = greedy.solve_greedy
    #
    # # Redux
    # solve_redux = redux.solve_redux
    #
    # # Dynamic
    # solve_dynamic = dynamic.dynamic
    #
    # # Redux
    # solve_fptas = FPTAS.fptas

    # Simulated cooling
    solve_sim = simulated.solve_sim


# Class to represent a maxterm.
# Maxterm holds configuration about everz variable. It can be in three distinct states
#  0 - variable not present in maxterm
#  1 - variable present
# -1 - variable present and negated
class Maxterm:
    # Constructor of maxterm
    def __init__(self, number_of_variables):
        self.number_of_variables = number_of_variables
        self.configuration = [0] * (number_of_variables + 1)  # configuration[0] is a dummy for a cleaner code
        self.configuration[0] = -420

    # Get variable set in format -3 (non C)
    def set(self, variable):
        if abs(variable) > (self.number_of_variables + 1):
            print("Cound not set a variable not present for this instance!")
            return False

        if variable >= 1:
            # Set to 1 -- Variable is present
            self.configuration[variable] = 1
        elif variable <= -1:
            # Set to -1 -- Variable is present AND NEGATED
            self.configuration[abs(variable)] = -1
        else:
            print("Found zero. This shoud be the end of line.")
            return False

        # print(self.configuration)

        return True

    # For listing things inside instance
    def __repr__(self):
        complete_string = "("
        first = True
        for i in range(0, self.number_of_variables + 1):
            if self.configuration[i] == 1:
                if first:
                    complete_string += "%d" % (i)
                    first = False
                    continue
                complete_string += " ∨ %d" % (i)
            elif self.configuration[i] == -1:
                if first:
                    complete_string += "¬%d" % (i)
                    first = False
                    continue
                complete_string += " ∨ ¬%d" % (i)

        complete_string += ")"
        return complete_string

    # Is the maxterm satisfied?
    def isSatisfiedWith(self, configuration):
        result = False
        for variable in self.configuration:
            if (variable == -420) or (variable == 0):
                continue
            elif variable == 1:
                result = configuration or result
            elif variable == -1:
                result = (not configuration) or result

        return result

    # Return Maxterm variables
    def getVars(self):
        return self.configuration


class CNFInstance:
    # Constructor of CNFInstance
    def __init__(self, id, number_of_variables):
        self.id = id
        self.number_of_variables = number_of_variables
        self.expecting_maxterms = -1
        self.number_of_maxterms = 0
        self.number_of_weights_set = 0

        self.weight_of_variables = [-1] * (
                number_of_variables + 1)  # weight_of_variables[0] is a dummy for cleaner code
        self.weight_of_variables[0] = -420
        self.maxterm_array = []

        self.best_weight = -1
        self.best_solution = [-420]  # Dummy on the [0] for consistence
        self.solved = False
        self.time = 0
        self.given_best_weight = -1
        self.given_best_solution = [-420]  # Dummy on the [0] for consistence

    def addMaxterm(self, maxterm):
        if maxterm.number_of_variables != self.number_of_variables:
            print("Could not maxterm with different number of variables!")
            return False
        self.maxterm_array.append(maxterm)
        self.number_of_maxterms += 1
        return True

    def setWeight(self, variable, weight):
        self.weight_of_variables[variable] = weight
        self.number_of_weights_set += 1
        return

    # For printing the instance
    def __str__(self):
        return "=== CNF Instance nr.%d ===\n" \
               "Variables     = %d\n" \
               "Weights       = %s\n" \
               "Maxterm array = %s\n" \
               "Best weight   = %d\n" \
               "Best solution = %s" % (
                   self.id, self.number_of_variables, self.weight_of_variables, self.maxterm_array, self.best_weight,
                   self.best_solution)

    # Simulated annealing
    solve_sim = simulated.solve_sim
