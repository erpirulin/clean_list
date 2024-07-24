user_answers = ["Yes", "", "No", "", "Maybe", "", "Yes"]

# Create a new list without empty answers
# using filter with a lambda expression
clean_list = list(filter(lambda name : name != "", user_answers))

# Display the cleaned list of answers
print(clean_list)
