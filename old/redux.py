def sort_ratio(thing):
    return thing.ratio


def sort_id(thing):
    return thing.sequence


def sort_value(thing):
    return thing.value


def solve_redux(self):
    self.complexity = 0

    # Sort array of stuff based on ratio
    # print(self.things_array)
    self.things_array.sort(key=sort_ratio, reverse=True)
    # Builder is only zeroes
    greedy_builder = [0] * self.current_things
    greedy_weight = 0
    greedy_cost = 0
    # Take stuff utill you run out of space
    for thing in self.things_array:
        self.complexity += 1
        # If I add one more will it be too much?
        if self.limit_weight < greedy_weight + thing.weight:
            break
        # Add new thing
        greedy_builder[thing.sequence] = 1
        greedy_weight = greedy_weight + thing.weight
        greedy_cost = greedy_cost + thing.value

    # Compare to the best value item that still fits
    redux_weight = 0
    redux_cost = 0
    redux_builder = [0] * self.current_things
    self.things_array.sort(key=sort_value, reverse=True)
    for thing in self.things_array:
        self.complexity += 1
        if thing.weight > self.limit_weight:
            # print("Cannot carry.")
            continue
        else:
            redux_cost = thing.value
            redux_weight = thing.weight
            redux_builder[thing.sequence] = 1
            # print("--- Found the best snatch. ---")
            print(redux_cost)
            break

    print("Is %d bigger than %d ?" % (redux_cost, greedy_cost) )
    if redux_cost > greedy_cost:
        print("Definetely yes")
        # Use redux
        self.best_solution = redux_builder
        self.best_cost = redux_cost
    else:
        print("Definetely no")
        # Use Greedy
        self.best_solution = greedy_builder
        self.best_cost = greedy_cost
    # Sort back to original order
    # self.things_array.sort(key=sort_id, reverse=False)
    return
