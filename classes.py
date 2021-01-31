import simulated


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

        j = -1
        for variable in self.configuration:
            j += 1
            if (variable == -420) or (variable == 0):
                continue
            elif variable == 1:
                # print("%r or %r" % (configuration[j], result))
                result = configuration[j] or result
            elif variable == -1:
                # print("%r or %r" % (not configuration[j], result))
                result = (not configuration[j]) or result

        return result

    # Return Maxterm variables
    def getVars(self):
        vars_of_maxterm = set()
        j = -1
        for var in self.configuration:
            j += 1
            if (var == -420) or (var == 0):
                continue
            elif (var == 1) or (var == -1):
                # print("Adding %d to set." % (j))
                vars_of_maxterm.add(j)

        return vars_of_maxterm


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
