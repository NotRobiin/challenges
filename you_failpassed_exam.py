def grade_percentage(got, required):
    int_required = required[: len(required) - 1]
    int_got = got[: len(got) - 1]

    if int_got >= int_required:
        return "You PASSED the Exam"

    return "You FAILED the Exam"


if __name__ == "__main__":
    print(grade_percentage("85%", "85%"))
