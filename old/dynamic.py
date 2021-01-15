import math  # for infinity
import copy  # for deep copy


def dynamic(self):
    self.complexity = 0
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

    # -- Cleanup --
    self.decompose_array = []
    self.decompose_builder = []
    return

