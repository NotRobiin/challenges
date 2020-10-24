relations = {
    "Person": "Relation",
    "Darth Vader": "father",
    "Leia": "sister",
    "Han": "brother in law",
    "R2D2": "droid",
}


def relation_to_luke(name):
    return "Luke, I am your %s." % (relations[name])


if __name__ == "__main__":
    print(relation_to_luke("Darth Vader"))
