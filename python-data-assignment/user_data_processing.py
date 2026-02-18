def calculate_average(users):
    for user in users:
        avg = sum(user["scores"]) / len(user["scores"])
        user["average"] = avg


def check_admin_access(roles):
    return "admin" in roles


def main():
    users = [
        {
            "name": "Alice",
            "scores": [80, 85, 90],
            "roles": {"admin", "editor"}
        },
        {
            "name": "Bob",
            "scores": [60, 70, 65],
            "roles": {"viewer"}
        }
    ]

    calculate_average(users)

    for user in users:
        print("\nName:", user["name"])
        print("Average Score:", user["average"])
        print("Admin Access:", check_admin_access(user["roles"]))


main()
