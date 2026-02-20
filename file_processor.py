def read_numbers(file_name):
    numbers = []
    with open(file_name, "r") as file:
        print("File opened successfully")
        for line in file:
            value = line.strip()
            if value:
                numbers.append(int(value))
    return numbers


def compute_values(numbers):
    total_count = len(numbers)
    total_sum = sum(numbers)
    average = total_sum / total_count if total_count > 0 else 0
    return total_count, total_sum, average


def write_log(log_file, message):
    with open(log_file, "a") as file:
        file.write(message + "\n")


def main():
    input_file = "numbers.txt"
    log_file = "results.log"

    numbers = read_numbers(input_file)
    write_log(log_file, "File opened successfully")
    write_log(log_file, f"Read {len(numbers)} numbers")

    count, total, avg = compute_values(numbers)

    write_log(log_file, f"Sum: {total}")
    write_log(log_file, f"Average: {avg}")
    write_log(log_file, "Processing completed")

    print("Processing completed. Check results.log file.")


main()
