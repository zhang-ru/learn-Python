import re
def parse_molecule (formula):
    a = re.findall(r"([A-Z][a-z]?)([0-9]?)",formula)
    b = re.findall("[\)|\]|\}]([1-9])",formula)

    return list(b)
print(parse_molecule('K4[ON(SO3)2]2'))