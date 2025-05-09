from agent2 import ask_tenancy_faq

if __name__ == "__main__":
    # Test 1: General FAQ
    question_1 = "Can my landlord increase rent during the lease?"
    response_1 = ask_tenancy_faq(question_1)
    print("Question 1:", question_1)
    print("Answer:", response_1)

    # Test 2: Location-specific
    question_2 = "What to do if the landlord is not returning my deposit?"
    location = "London, UK"
    response_2 = ask_tenancy_faq(question_2, location=location)
    print("\nQuestion 2:", question_2)
    print("Location:", location)
    print("Answer:", response_2)
