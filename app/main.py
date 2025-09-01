class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people: list) -> list:
    results = []
    for person in people:
        new_person = Person(person["name"], person["age"])
        results.append(new_person)

    for person in people:
        if "wife" in person and person["wife"] is not None:
            new_person = next(
                item for item in results if item.name == person["name"]
            )
            new_person.wife = next(
                item for item in results if item.name == person["wife"]
            )

        if "husband" in person and person["husband"] is not None:
            new_person = next(
                item for item in results if item.name == person["name"]
            )
            new_person.husband = next(
                item for item in results if item.name == person["husband"]
            )
    return results
