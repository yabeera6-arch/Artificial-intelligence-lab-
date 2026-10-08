# Reliability Test for Scholarship Decision System

def scholarship_decision(score, documents, attendance, recommendation):
    return (
        score >= 70
        and documents
        and attendance >= 75
        and recommendation
    )


# Known correct test cases
test_cases = [
    (85, True, 80, True, True),
    (69, True, 80, True, False),
    (70, True, 75, True, True),
    (90, False, 90, True, False),
    (80, True, 74, True, False),
    (80, True, 80, False, False)
]

correct = 0

for i, case in enumerate(test_cases, 1):

    score, documents, attendance, recommendation, expected = case

    actual = scholarship_decision(
        score,
        documents,
        attendance,
        recommendation
    )

    print("Case", i)
    print("Expected:", expected)
    print("Actual:", actual)

    if actual == expected:
        print("PASS")
        correct += 1
    else:
        print("FAIL")

    print("--------------------")


accuracy = (correct / len(test_cases)) * 100

print("Accuracy:", accuracy, "%")