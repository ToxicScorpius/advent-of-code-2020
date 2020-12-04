passport = {}
required_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
valid_passports, r_fields_count = 0, 0

with open("day4_input.txt") as file:
    for line in file:
        for field in line.split():
            key, val = field.split(":")
            if key in required_fields:
                r_fields_count += 1
            passport.update({key: val})

        if line == "\n":
            if r_fields_count == 7:
                valid_passports += 1
            r_fields_count = 0
            passport.clear()
    print(valid_passports)
