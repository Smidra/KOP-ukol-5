def sort_ratio(thing):
    return thing.ratio


def sort_id(thing):
    return thing.sequence


def solve_greedy(self):
    # Sort array of stuff based on ratio
    # print(self.things_array)
    self.things_array.sort(key=sort_ratio, reverse=True)
    # Builder is only zeroes
    builder = [0] * self.current_things
    current_weight = 0
    current_cost = 0
    # Take stuff utill you run out of space
    for thing in self.things_array:
        # If I add one more will it be too much?
        if self.limit_weight < current_weight + thing.weight:
            break
        # Add new thing
        builder[thing.sequence] = 1
        current_weight = current_weight + thing.weight
        current_cost = current_cost + thing.value

    # print(builder)
    self.best_solution = builder
    self.best_cost = current_cost

    # Sort back to original order
    # self.things_array.sort(key=sort_id, reverse=False)
    # print(self.things_array)
    # print("")
    # self.complexity_brute = 0
    # builder = []
    # self.brute(self.limit_weight, self.min_cost, 0, 0, builder)
    return
