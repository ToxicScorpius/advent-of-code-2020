import re

passport = {}
valid_passports, valid_fields, r_fields_count = 0, 0, 0

required_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
possible_ecl_val = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
convert_to_int = {"byr", "iyr", "eyr"}

regex_hgt = re.compile(r"^(\d+)(cm|in)$")
regex_hgt_val = re.compile(r"^[0-9]")
regex_hgt_unit = re.compile(r"cm$|in$")
regex_hcl = re.compile(r"#[0-9a-f]{6}")
regex_pid = re.compile(r"^\d{9}$")

with open("day4_input.txt") as file:
    for line in file:
        for field in line.split():
            key, val = field.split(":")
            if key in convert_to_int:
                val = int(val)
            if key in required_fields:
                r_fields_count += 1
            passport.update({key: val})

        if line == "\n":
            if r_fields_count == 7:
                for key, val in passport.items():
                    if key == "byr":
                        if 2002 >= val >= 1920:
                            valid_fields += 1

                    if key == "iyr":
                        if 2020 >= val >= 2010:
                            valid_fields += 1

                    if key == "eyr":
                        if 2030 >= val >= 2020:
                            valid_fields += 1

                    if key == "hgt":
                        if regex_hgt.match(val):
                            height_str = regex_hgt.match(val)
                            height, unit = height_str.groups()
                            height = int(height)
                            if unit == "cm":
                                if 193 >= height >= 150:
                                    valid_fields += 1
                            if unit == "in":
                                if 76 >= height >= 59:
                                    valid_fields += 1

                    if key == "hcl":
                        if regex_hcl.match(val):
                            valid_fields += 1

                    if key == "ecl":
                        if val in possible_ecl_val:
                            valid_fields += 1

                    if key == "pid":
                        if regex_pid.match(val):
                            valid_fields += 1

            if valid_fields == 7:
                valid_passports += 1
            r_fields_count, valid_fields = 0, 0
            passport.clear()
    print(valid_passports)
