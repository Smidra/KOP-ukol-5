import copy  # for deep copy


# Solve the instance brute force
def solve_brute(self):
    self.complexity_brute = 0
    self.complexity = 0
    builder = []
    self.brute(self.limit_weight, self.min_cost, 0, 0, builder)
    return


# Brute force recursion function
def brute(self, lim_weight, min_cost, total_cost, size, solution_builder):
    # Is it a leaf? (End recursion)
    if size == self.current_things:
        # print("Leaf %s reached. Total cost=%d" % (solution_builder, total_cost))
        # Is the leaf light enough? AND Is it the best cost of all leaves?
        if (lim_weight >= 0) and (total_cost > self.best_cost):
            self.best_cost = total_cost
            self.best_solution = solution_builder
            # print("New best is %d" % self.best_cost)

            # Is the leaf worth it? AND Is it the best solution?
            if (total_cost >= min_cost) and (total_cost > self.best_cost):
                self.best_acceptable_cost = total_cost
                self.best_acceptable_solution = solution_builder
                # print("New acceptable best is %d" % self.best_cost)

        # Complexity +1
        self.complexity_brute = self.complexity_brute + 1
        self.complexity += 1
        return


    # We will take it (1)
    tmp = copy.copy(solution_builder)
    tmp.append(1)
    self.brute(lim_weight=lim_weight - self.things_array[size].weight,
               min_cost=min_cost,
               total_cost=total_cost + self.things_array[size].value,
               size=size + 1,
               solution_builder=tmp)

    # We will leave it (0)
    tmp = copy.copy(solution_builder)
    tmp.append(0)
    self.brute(lim_weight=lim_weight,
               min_cost=min_cost,
               total_cost=total_cost,
               size=size + 1,
               solution_builder=tmp)

    return
