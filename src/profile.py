intern_name = "Sagar Maurya"
role = "Software Engineering Intern"
department = "Engineering"

skills = [
    "Python",
    "Django",
    "Git",
    "REST API",
    "SQL"
]


def print_profile():
    print("----- Intern Profile -----")
    print(f"Name: {intern_name}")
    print(f"Role: {role}")
    print(f"Department: {department}")
    print("Skills:")

    for skill in skills:
        print(f"- {skill}")


if __name__ == "__main__":
    print_profile()


def get_profile():
    return {
        "name": intern_name,
        "role": role,
        "department": department,
        "skills": skills
    }