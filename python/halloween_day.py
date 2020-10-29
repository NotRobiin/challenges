def halloween(date):
    month = date[5:7]
    day = date[8:10]

    if month == "10" and day == "31":
        return "Bonfire toffee"

    return "toffee"


if __name__ == "__main__":
    print(halloween("2013/10/31"))
