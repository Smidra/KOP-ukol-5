import copy  # for deep copy


# Solve the instance brute force with cutting
def solve_branch_and_bound(self):
    self.complexity = 0
    builder = []
    self.branch_and_bound(self.limit_weight, self.min_cost, 0, 0, builder, self.value_of_all)
    return


# Brute force (with weight cutting) recursion function
def branch_and_bound(self, lim_weight, min_cost, total_cost, size, solution_builder, best_case_value):
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
        # !!! Branch & bound writes to COMPLEXITY, not COMPLEXITY_BRUTE
        self.complexity = self.complexity + 1
        return

    # Neni treba volat ani jednu z dalsich vetvi, kdyz
    # celkova hodnota toho co je pode mnou + moje hodnota JE HORSI nez neco co jsem nasel

    # It is not nescessary to go deeper.
    # Even the best possible solution from this branch
    # Is still worse than something I found
    if (best_case_value + total_cost) <= self.best_cost :
        return

    # We will try take it (1)
    # Is the knapsack full already? (cutting based of weight)
    if (lim_weight >= 0):
        tmp = copy.copy(solution_builder)
        tmp.append(1)
        self.branch_and_bound(lim_weight=lim_weight - self.things_array[size].weight,
                              min_cost=min_cost,
                              total_cost=total_cost + self.things_array[size].value,
                              size=size + 1,
                              solution_builder=tmp,
                              best_case_value=best_case_value-self.things_array[size].value)

    # We will leave it (0)
    tmp = copy.copy(solution_builder)
    tmp.append(0)
    self.branch_and_bound(lim_weight=lim_weight,
                          min_cost=min_cost,
                          total_cost=total_cost,
                          size=size + 1,
                          solution_builder=tmp,
                          best_case_value=best_case_value-self.things_array[size].value)

    return
