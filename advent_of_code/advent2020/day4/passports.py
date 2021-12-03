import re
from typing import Callable, Dict, List


def validate_hgt(s: str) -> bool:
    """
    hgt (Height) - a number followed by either cm or in:
    If cm, the number must be at least 150 and at most 193.
    If in, the number must be at least 59 and at most 76.
    """
    height = s[:-2]
    unit = s[-2:]
    result = False
    if unit in ["cm", "in"] and height.isnumeric():
        if unit == "cm":
            result = 150 <= int(height) <= 193
        else:
            result = 59 <= int(height) <= 76
    return result


validation_rules = {
    # byr (Birth Year) - four digits; at least 1920 and at most 2002.
    "byr": lambda s: 1920 <= int(s) <= 2002,
    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    "iyr": lambda s: 2010 <= int(s) <= 2020,
    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    "eyr": lambda s: 2020 <= int(s) <= 2030,
    "hgt": validate_hgt,
    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    "hcl": lambda s: s[0] == "#" and len(s) == 7 and re.match(r"[0-9a-f]", s[1:]),
    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    "ecl": lambda s: s.strip() in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    "pid": lambda s: len(s) == 9 and s.isnumeric(),
    # cid (Country ID) - ignored, missing or not.
}


simple_validation_rules = {
    k: (lambda _: True)
    for k in validation_rules.keys()
    # "byr": (lambda _: True),
    # "iyr": (lambda _: True),
    # "eyr": (lambda _: True),
    # "hgt": (lambda _: True),
    # "hcl": (lambda _: True),
    # "ecl": (lambda _: True),
    # "pid": (lambda _: True),
}


def parse_single_batch(batch: List[str]) -> Dict[str, str]:
    result = {}
    for item in batch:
        x = item.split(":")
        result[x[0]] = x[1]
    return result


def passport_is_valid(
    passport: Dict[str, str], rules: Dict[str, Callable[[str], bool]]
) -> bool:
    result = True
    for key, rule in rules.items():
        if not (key in passport and rule(passport[key])):
            result = False
    return result


def count_valid_passports(
    contents: str, rules: Dict[str, Callable[[str], bool]]
) -> int:
    contents = contents.strip()

    blocks = contents.split("\n\n")
    num_valid = 0

    for block in blocks:
        block = block.replace("\n", " ")
        unparsed_batch = block.split(" ")
        parsed_batch = parse_single_batch(unparsed_batch)

        if passport_is_valid(parsed_batch, rules):
            num_valid += 1

    return num_valid
