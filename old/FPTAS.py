import math  # for infinity
import copy  # for deep copy


def fptas(self, epsilon):
    self.complexity = 0
    # -- Prepare values for FPTAS --
    # Calculate biggest price
    # If thing is heavier than knapsack can carry disregard it
    c_max = -1
    for thing in self.things_array:
        if thing.weight > self.limit_weight:
            # print("%d > %d" % (thing.weight, self.limit_weight) )
            thing.weight = -1
            continue
        if thing.value > c_max:
            c_max = thing.value

    # If nothing can be added to the knapsack, end
    if c_max == -1:
        self.best_cost_reduced = 0
        self.best_cost = 0
        # -- Cleanup --
        self.decompose_array = []
        self.decompose_builder = []
        return

    # Calclulate K
    k = 0
    while True:
        k = float(epsilon * c_max) / float(self.current_things)
        k = int(k)
        # If K is too small with this epsilon, try with a slightly bigger epsilon.
        if k != 0:
            break
        epsilon += 0.01

    # Reduce costs of all things
    total_cost = 0
    for thing in self.things_array:
        thing.value = int(thing.value / k)
        if thing.weight != -1:
            total_cost += thing.value

    self.value_of_all = total_cost

    # -- Create arrays --
    # Array for cost decomposition
    # self.decompose_array[1053][2] - [CENA][VEC]
    w, h = self.current_things + 1, self.value_of_all + 1
    self.decompose_array = [[math.inf] * w for i in range(h)]
    self.decompose_array[0][0] = 0
    # Array for constructing solution
    self.decompose_builder = [[[]] * w for i in range(h)]

    # -- Fill array --
    # For each thing in knapsack
    for thing_nr in range(0, self.current_things):
        current_thing = self.things_array[thing_nr]
        # For every cost in this column
        for cost_nr in range(0, self.value_of_all + 1):
            current_cell = self.decompose_array[cost_nr][thing_nr]
            # Is it a possible outcome?
            if self.decompose_array[cost_nr][thing_nr] != math.inf:
                # print("Possible outcome: %d %d" % (cost_nr, thing_nr))
                # print("self.decompose_array[%d][%d]" % (cost_nr + current_thing.value, thing_nr+1))

                # Add thing
                if current_thing.weight != -1: # Skip items bigger than knapsack
                    add_cell = self.decompose_array[cost_nr + current_thing.value][thing_nr + 1]
                    if current_cell + current_thing.weight < add_cell:
                        self.complexity += 1
                        # My solution is better than currently present solution
                        # Otherwise what was in there was a better solution
                        self.decompose_array[cost_nr + current_thing.value][
                            thing_nr + 1] = current_cell + current_thing.weight
                        tmp = copy.copy(self.decompose_builder[cost_nr][thing_nr])
                        tmp.append(1)
                        self.decompose_builder[cost_nr + current_thing.value][thing_nr + 1] = tmp

                # Do not add thing
                not_add_cell = self.decompose_array[cost_nr][thing_nr + 1]
                if current_cell < not_add_cell:
                    self.complexity += 1
                    # My solution is better than currently present solution
                    # Otherwise what was in there was a better solution
                    self.decompose_array[cost_nr][thing_nr + 1] = current_cell
                    tmp = copy.copy(self.decompose_builder[cost_nr][thing_nr])
                    tmp.append(0)
                    self.decompose_builder[cost_nr][thing_nr + 1] = tmp

                # self.decompose_array[cost_nr + current_thing.value][thing_nr + 1] = min(add_cell,
                #                                                                         current_cell + current_thing.weight)
                # self.decompose_array[cost_nr][thing_nr + 1] = min(not_add_cell, current_cell)

                # print("+ Add %d to %d %d" % (
                #     min(add_cell, current_cell + current_thing.weight), cost_nr + current_thing.value, thing_nr + 1))
                # print("- Add %d to %d %d" % (
                #     min(not_add_cell, current_cell), cost_nr, thing_nr + 1))

    # self.print_decompose()

    # -- Find solution --
    cost = -1
    # Iterate tle last column of cost decomposition
    for i in self.decompose_array:
        cost += 1
        if i[w - 1] <= self.original_limit_weight and i[w - 1] != -1:
            # Found possible knapsack configuration
            if cost > self.best_cost:
                self.best_cost = cost

    self.best_solution = self.decompose_builder[self.best_cost][self.current_things]
    self.best_cost_reduced = self.best_cost
    self.best_cost = self.best_cost * k

    # -- Cleanup --
    self.decompose_array = []
    self.decompose_builder = []
    return
