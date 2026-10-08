# Rule-Based Scholarship Eligibility System

def scholarship_decision(score, document_complete,
                         attendance, recommendation_letter):

    # Condition 1
    score_ok = score >= 70

    # Condition 2
    documents_ok = document_complete

    # Condition 3
    attendance_ok = attendance >= 75

    # Condition 4
    recommendation_ok = recommendation_letter

    # Final decision
    if score_ok and documents_ok and attendance_ok and recommendation_ok:
        return "Eligible"

    else:
        return "Not Eligible"


# Test Cases

test_cases = [
    # Case 1: All conditions pass
    {
        "name": "Test Case 1",
        "score": 85,
        "document_complete": True,
        "attendance": 80,
        "recommendation_letter": True,
        "expected": "Eligible"
    },

    # Case 2: Attendance fails
    {
        "name": "Test Case 2",
        "score": 85,
        "document_complete": True,
        "attendance": 70,
        "recommendation_letter": True,
        "expected": "Not Eligible"
    },

    # Case 3: Recommendation letter fails
    {
        "name": "Test Case 3",
        "score": 85,
        "document_complete": True,
        "attendance": 80,
        "recommendation_letter": False,
        "expected": "Not Eligible"
    },

    # Case 4: Boundary values
    {
        "name": "Test Case 4",
        "score": 70,
        "document_complete": True,
        "attendance": 75,
        "recommendation_letter": True,
        "expected": "Eligible"
    }
]


# Run all test cases

for case in test_cases:

    actual = scholarship_decision(
        case["score"],
        case["document_complete"],
        case["attendance"],
        case["recommendation_letter"]
    )

    print(case["name"])
    print("Expected:", case["expected"])
    print("Actual:", actual)

    if actual == case["expected"]:
        print("Result: PASS")
    else:
        print("Result: FAIL")

    print("-------------------------")
