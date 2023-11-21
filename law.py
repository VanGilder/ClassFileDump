clarkesLaws = "1) When a distinguished but elderly scientist states that something is possible, he is almost certainly right. When he states that something is impossible, he is very probably wrong.\n\n2) The only way of discovering the limits of the possible is to venture a little way past them into the impossible.\n\n3) Any sufficiently advanced technology is indistinguishable from magic.\n\n"

print(clarkesLaws)

user_data = input("Enter the law number you would like to quote (1, 2, or 3): ")

if user_data != "1" and user_data != "2" and user_data != "3":
    print("Error, invalid option: " + user_data + ". Please choose 1, 2, or 3. Exiting.")
    exit(0)

looking_for = user_data + ") "
start_index = clarkesLaws.index(looking_for)

start_index += 3

end_index = clarkesLaws.index("\n\n", start_index)
law = clarkesLaws[start_index:end_index]

quote = f'"{law}" -- Arthur C. Clarke'
print()
print(quote)


