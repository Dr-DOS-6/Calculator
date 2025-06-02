import ast
import multiprocessing
from itertools import chain, combinations

def parse_set(input_str):
    """Parse the input string into a Python set."""
    try:
        # Convert the string to a set using ast.literal_eval
        return set(ast.literal_eval(input_str.replace("{", "{").replace("}", "}")))
    except Exception as e:
        raise ValueError("Invalid input format. Please use the format: \"{num1,num2,num3}\"") from e

def power_set(s):
    """Generate the power set of a given set."""
    return set(frozenset(subset) for subset in chain.from_iterable(combinations(s, r) for r in range(len(s) + 1)))

def parallel_power_set(sets):
    """Generate the power set of multiple sets in parallel."""
    with multiprocessing.Pool() as pool:
        results = pool.map(power_set, sets)
    return set(chain.from_iterable(results))

def main():
    input_str = input("Enter a set in the format \"{num1,num2,num3}\": ")
    try:
        original_set = parse_set(input_str)
        print(f"Original set: {original_set}")
        
        # Generate the first power set
        first_power_set = power_set(original_set)
        print(f"First power set: {first_power_set}")
        
        # Generate the second power set
        second_power_set = power_set(first_power_set)
        print(f"Second power set: {second_power_set}")
        
        # Generate the third power set in parallel
        third_power_set = parallel_power_set(second_power_set)
        print(f"Third power set: {third_power_set}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()