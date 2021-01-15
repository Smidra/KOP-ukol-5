import sys  # work with arguments
from classes import *  # Custom made classes file
import time
import os  # For getting files in the directory


# python main.py ${KDE_JE_ZADANI} ${KAM_ULOZIT_VYSLEDKY}     ${KDE_JE_KONTROLNI_VYSLEDEK}
# python main.py ${1}             ${2}                       ${3}
#                SLOŽKA           SLOŽKA                     SOUBOR

# Read arguments, control program flow
def main():
    # Load instances from file to objects
    instances_array = load_instances_file(sys.argv[1])
    load_solution_file(sys.argv[3], instances_array)
    save_complexity_file(sys.argv[2], instances_array)
    exit(1)

    # Solve every instance
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

    # Save the constructed solutions for diff comparison
    save_solution_file(sys.argv[2], instances_array)
    # Save the calculated complexity
    save_complexity_file(sys.argv[2], instances_array)

    better_output(sys.argv[4], instances_array, sys.argv[5])
    return


# Sorting array of pairs is a bit complicated in python
# https://www.pythoncentral.io/how-to-sort-a-list-tuple-or-object-with-sorted-in-python/
def getKey(item):
    return int(item[1])


# Load instances from file to objects in array
def load_instances_file(directory_location):
    instances_array = []

    # Get all the available problems in specified folder
    # For every file in the folder get filename and parse out the ID
    files_in_dir = os.listdir(directory_location)
    problems = []  # Save parsed IDs here
    for file in files_in_dir:
        file_variables = file.split('.', 1)[0].split('-')[0].split('f')[
            1]  # Splitting filename to get number of variables
        file_id = str(file.split('.', 1)[0].split('-')[1])  # Splitting filename to get instance ID
        problems.append((file_variables, file_id))
    problems.sort(key=getKey)  # Soring array of pairs by the second parameter
    # print(problems)

    # Load every problem into a CNF Instance
    for problem in problems:
        # Create CNFInstance, set Instance ID, set number of variables
        number_of_variables = int(problem[0])
        problem_id = int(problem[1])
        new_instance = CNFInstance(problem_id, number_of_variables)
        # From file read number of maxterms, weights, and maxterms themselves
        # ... and construct the new instance to be as read from file
        file_location = directory_location + "/wuf%s-%s.mwcnf" % (number_of_variables, problem[1])
        f = open(file_location, "r")
        line_nr = 0
        for line in f:
            line_nr += 1
            line = line.split()

            # Parse number of maxterms
            if line_nr == 8:
                new_instance.expecting_maxterms = int(line[3]) - 1
                continue
            # Parse weights
            if line_nr == 10:
                j = 0
                for weight in line:
                    # Skip unneded stuff on line
                    if weight == '0' or weight == 'w':
                        continue
                    j += 1
                    new_instance.setWeight(j, int(weight))
                continue
            # Parse maxterms one by one
            elif line_nr >= 12:
                # Create new maxterm
                m = Maxterm(number_of_variables)
                # Build maxterms and ignore zero at end of line.
                for i in line:
                    if i != '0':
                        m.set(int(i))
                # Add maxterm to instance
                new_instance.addMaxterm(m)
                continue
            else:
                continue

        # Check if all Maxterms loaded succesfully into instance and if all weights loaded succecfully.
        if (new_instance.number_of_maxterms != new_instance.expecting_maxterms) or (
                new_instance.number_of_weights_set != new_instance.number_of_variables):
            # Do not add instance into instance array.
            print("Did not get the expected number of maxterms when loading instance number %d." % (problem_id))
        else:
            # print(new_instance)
            print("Loaded instance: %d" % (problem_id))
            # Append new instance to instances_array.
            instances_array.append(new_instance)

    return instances_array


# Load solutions from file to instances
def load_solution_file(solution_file_location, instances_array):
    # Open file
    f = open(solution_file_location, "r")
    # For each line, parse the needed info
    for line in f:
        line = line.split()
        # Load solution ID and find the corresponding instance
        instance_id = int(line[0].split('-')[1])
        for instance in instances_array:
            if instance.id == instance_id:
                this_id_instance = instance

        # Load given exact best solution, and given best weight into the instace
        this_id_instance.given_best_weight = int(line[1])

        j = 1
        while True:
            j += 1
            variable = int(line[j])
            if variable == 0:
                break
            # Add each variable of solution to new instance
            if variable > 0:
                this_id_instance.given_best_solution.append(1)
            elif variable < 0:
                this_id_instance.given_best_solution.append(-1)
            else:
                print("Very bad. It looks like variable in solution is 0.")

        # print("Loaded solution for Instance nr %d:" % (this_id_instance.id))
        # print(this_id_instance.given_best_solution)

    return


# Save CONSTRUCTED solved solution of instances to a file
# The solution file is formatted the same as MOODLE solutions
# Diff can than easily spot differences
def save_solution_file(file_location, instances_array):
    f = open(file_location + "/solution_%d.dat" % (instances_array[0].number_of_variables), "w")
    for instance in instances_array:
        # uf20-01000 5738 -1 2 3 4 5 6 7 8 9 10 -11 12 13 14 -15 -16 -17 18 19 -20 0
        f.write("uf%d-0%d %d" % (instance.number_of_variables, instance.id, instance.best_weight))
        j = -1
        for config in instance.best_solution:
            j += 1
            if config == -420:
                continue
            elif config == 1:
                f.write(" %d" % j)
            elif config == 0:
                f.write(" %d" % (-1 * j))
            else:
                print("Configuration in calculated solution is unexpected!")
                print(config)

        f.write(" 0 \n")

    f.close()
    return


# Save all info about complexity of calculated instances to a file
def save_complexity_file(file_location, instances_array):
    f = open(file_location + "/complexity_%d.dat" % (instances_array[0].number_of_variables), "w")
    time_sum = 0
    max_time = -1
    error_sum = 0
    max_error = -1
    instances_sum = 0
    for instance in instances_array:
        # Find max and avg time
        if instance.time > max_time:
            max_time = instance.time
        time_sum += instance.time
        # Find max and avg error
        current_error = abs(instance.best_weight - instance.given_best_weight)
        if current_error > max_error:
            max_error = current_error
        error_sum += current_error
        # Print the complexity file
        f.write("%d\t%d\t%d\t%d\t%f\n" % (instance.id,
                                      instance.best_weight,
                                      instance.given_best_weight,
                                      current_error,
                                      instance.time))
        instances_sum += 1

    avg_time = float(time_sum) / instances_sum
    avg_error = error_sum / instances_sum
    f.write("================ Summary ================\n"
            "Time  avg max:\t%f\t%f\n"
            "Error avg max:\t%d\t\t%d\n" % (avg_time, max_time, avg_error, max_error))

    print("================ Summary ================")
    print("Time  avg max:\t%f\t%f" % (avg_time, max_time))
    print("Error avg max:\t%d\t\t%d" % (avg_error, max_error))
    f.close()


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


if __name__ == '__main__':
    main()
