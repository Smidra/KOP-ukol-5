import sys  # work with arguments
from classes import *  # Custom made classes file
import time


# python main.py ${KDE_JE_ZADANI} ${KAM_ULOZIT_VYSLEDKY}     ${KDE_JE_KONTROLNI_VYSLEDEK}
# python main.py ${1}             ${2}                       ${4}
#                SLOŽKA           SLOŽKA                     SOUBOR

# Read arguments, control program flow
def main():
    # Load instances from file to objects
    instances_array = load_instances_file(sys.argv[1])

    # Solve every instance
    # for i in range(3, 4):
    for i in range(0, file_len(sys.argv[1])):
        start = time.process_time()
        if sys.argv[6] == "sim":
            instances_array[i].solve_sim(30, 0.97)
        else:
            print("Pick a valid instance from: brute, bab, greedy, redux, dynamic, fptas3, sim")

        end = time.process_time()
        # print("Elapsed time is %f" % (float(end-start)))
        instances_array[i].time = float(end - start)
        print(instances_array[i])

    # Save the constructed solution for diff comparison
    save_solution_file(sys.argv[2], instances_array)
    # Save the calculated complexity
    save_complexity_file(sys.argv[3], instances_array)

    better_output(sys.argv[4], instances_array, sys.argv[5])
    return


# Load instances from file to objects in array
def load_instances_file(directory_location):
    instances_array = []

    m = Maxterm(5)
    m.set(-1)
    m.set(2)
    m.set(-5)
    print(m)
    exit(1)

    # For every file in the folder

    # Open the file
    # Create CNFInstance
    # Set Instance ID
    # Set number of variables
    # Set variables weight
    # Add maxterms to instance

    # Append new instance to instances_array


    # Open file with instances
    f = open(directory_location, "r")

    # Iterate, create KnapsackInstance from each line and add them to instances_array
    for line in f:
        line = line.split()
        # Create new KnapsackInstance
        new_inst = KnapsackInstance(id=1 * int(line[0]),
                                    expecting_things=int(line[1]),
                                    limit_weight=int(line[2]),
                                    min_cost=int(-1))
        # Iterate the rest of the line to create and load Things
        for i in range(1, int(line[1]) + 1):
            new_thing = Thing(int(line[(i * 2) + 1]), int(line[(i * 2) + 2]))
            new_inst.add_thing(new_thing)

        # Add the constructed KnapsackInstance to an array representing the file
        instances_array.append(new_inst)

    return instances_array


# Count lines in a file
# Source: https://stackoverflow.com/questions/845058/how-to-get-line-count-of-a-large-file-cheaply-in-python
def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


# Better output
def better_output(solution_location, instances_array, save_summary):
    # Open file with instances
    try:
        f = open(solution_location, "r")
    except:
        print("======================")
        print("This is python. Sorry but %s does not exist." % (solution_location))
        return

    item_nr = 0
    max_complexity = 0
    avg_complexity = 0
    max_error = 0
    avg_error = 0

    for line in f:
        line = line.split()
        if instances_array[item_nr].id != int(line[0]):
            # print("Item nr> %d != %d <Currently reading" % (item_nr+1, int(line[0])))
            continue
        correct_solution = line[2]
        calculated_solution = instances_array[item_nr].best_cost
        if int(correct_solution) != 0:
            absolute_calculation_error = abs(calculated_solution - int(correct_solution))
            one_percent = float(float(correct_solution) / 100)
            # print("One percent from %d is %f" % ( int(correct_solution), one_percent ) )
            calculation_error = float(absolute_calculation_error / one_percent)
        calculation_complexity = instances_array[item_nr].complexity
        max_error = max(max_error, calculation_error)
        max_complexity = max(max_complexity, calculation_complexity)
        avg_complexity += calculation_complexity
        avg_error += calculation_error
        item_nr += 1

    avg_error = float(avg_error) / float(len(instances_array))
    avg_complexity = float(avg_complexity) / float(len(instances_array))

    print("%f; %f; %f; %f --> complexity max, complexity avg, max error, avg error." % (
        max_complexity, avg_complexity, max_error, avg_error))

    f = open(save_summary, "a")
    f.write("%d; %f; %f; %f; %f\n" % (
        instances_array[0].current_things, max_complexity, avg_complexity, max_error, avg_error))
    f.close()

    return


# Save CONSTRUCTED solved instances to a file
# The solution file is formatted the same as MOODLE solutions
# Diff can than easily spot differences
def save_solution_file(file_location, instances_array):
    f = open(file_location, "w")
    for instance in instances_array:
        f.write("%d %d %d" % (instance.id, instance.current_things, instance.best_cost))
        for config in instance.best_solution:
            f.write(" %d" % config)

        f.write(" \n")

    f.close()
    return


# Save all info about complexity of calculated instances to a file
def save_complexity_file(file_location, instances_array):
    f = open(file_location, "w")
    # time_sum = 0
    # complexity_sum = 0
    # brut_sum = 0
    for instance in instances_array:
        f.write("%d %d %d %d %d %f\n" % (instance.id,
                                         instance.best_cost,
                                         instance.best_acceptable_cost,
                                         instance.complexity,
                                         instance.complexity_brute,
                                         instance.time))
        # complexity_sum = complexity_sum + instance.complexity
        # brut_sum = brut_sum + instance.complexity_brute
        # time_sum = time_sum + instance.time

    # print("====== Summary ======")
    # print("Avg time:  %d" % (float(time_sum) / len(instances_array)))
    # print("Avg complexity:  %d" % (int(complexity_sum) / len(instances_array)))
    # print("Avg brute:  %d" % (int(brut_sum) / len(instances_array)))
    f.close()


if __name__ == '__main__':
    main()
