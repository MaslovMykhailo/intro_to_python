from typing import List, Dict, TypedDict


class Company(TypedDict):
    name: str
    hq: str


def assignment_1() -> Dict[str, List[str]]:
    companies = [
        {"name": "Apple", "hq": "Cupertino, California"},
        {"name": "Google", "hq": "Mountain View, California"},
        {"name": "Netflix", "hq": "Los Gatos, California"},
    ]

    def get_company_names_for_loop(companies: List[Company]) -> List[str]:
        company_names = []
        for company in companies:
            company_names.append(company["name"])
        return company_names

    def get_company_names_list_comprehension(companies: List[Company]) -> List[str]:
        return [company["name"] for company in companies]

    return {
        "for_loop": get_company_names_for_loop(companies),
        "list_comprehension": get_company_names_list_comprehension(companies),
    }


def assignment_2():
    companies = ["netflix", "apple", "apple", "google"]

    def remove_duplicates(input: List[str]) -> List[str]:
        dictionary = {}
        output = []

        for value in input:
            if value in dictionary:
                continue

            dictionary[value] = True
            output.append(value)

        return output

    return {"no_duplicates": remove_duplicates(companies)}


def assignment_3():
    keys = ["name", "hq", "no_employees", "established"]
    values = ["Apple", "Cupertino, California", 161000, 1976]

    def create_from_entries_for_loop(keys: List[str], values: List[str]) -> Dict[str, str]:
        dictionary = {}
        size = min(len(keys), len(values))
        for index in range(size):
            dictionary[keys[index]] = values[index]
        return dictionary

    def create_from_entries_zip(keys: List[str], values: List[str]) -> Dict[str, str]:
        return dict(zip(keys, values))

    return {
        "for_loop": create_from_entries_for_loop(keys, values),
        "zip": create_from_entries_zip(keys, values),
    }
