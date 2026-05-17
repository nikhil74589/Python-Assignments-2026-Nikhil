# UPSC Selection Process

# Eligibility Check :
age = int(input("Enter your age: "))
graduate = input("Are you a graduate? (yes/no): ")
nationality = input("Enter your nationality: ")

if age >= 21 and age <= 32:
    if graduate.lower() == "yes":
        if nationality.lower() == "Indian":

            print("Eligible for UPSC. Proceed to Prelims.")

            # Prelims Exam
            prelims_score = int(input("Enter Prelims score: "))
            prelims_cutoff = 60

            if prelims_score >= prelims_cutoff:
                print("You passed the Prelims. Proceed to Mains.")

                # Mains Exam
                mains_score = int(input("Enter Mains score: "))
                mains_cutoff = 70

                if mains_score >= mains_cutoff:
                    print("You passed the Mains. Proceed to Interview.")

                    # Interview
                    interview_score = int(input("Enter Interview score: "))
                    interview_cutoff = 50

                    if interview_score >= interview_cutoff:
                        print("Congratulations! You have cleared the UPSC.")
                    else:
                        print("You failed the Interview.")

                else:
                    print("You failed the Mains.")

            else:
                print("You failed the Prelims.")

        else:
            print("Ineligible: Nationality must be Indian.")
    else:
        print("Ineligible: Candidate must be a graduate.")
else:
    print("Ineligible: Age must be between 21 and 32 years.")