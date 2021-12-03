from advent2020.common import input_path
from advent2020.day4.passports import (
    count_valid_passports,
    simple_validation_rules,
    validation_rules,
)
import pytest


def simple_batch_file() -> str:
    return """
ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
"""


def full_batch_file() -> str:
    with open(input_path(__file__), "r") as file:
        return file.read()


@pytest.mark.parametrize(
    "batch_file,rules,expected",
    [
        (simple_batch_file(), simple_validation_rules, 2),
        (simple_batch_file(), validation_rules, 2),
        (full_batch_file(), simple_validation_rules, 256),
        (full_batch_file(), validation_rules, 198),
    ],
)
def test_count_valid_passports(batch_file, rules, expected):
    result = count_valid_passports(batch_file, rules)
    assert expected == result
