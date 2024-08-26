def main():
    # Initialize the number of total tickets and the ticket limit per buyer
    total_tickets = 20
    ticket_limit = 4
    total_buyers = 0  # Accumulator for the number of buyers

    # Loop until all tickets are sold
    while total_tickets > 0:
        # Prompt user for the desired number of tickets
        try:
            tickets_requested = int(input("Enter the number of tickets you want to buy (up to 4): "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        # Check if the requested number of tickets is within the allowed limit
        if tickets_requested < 1 or tickets_requested > ticket_limit:
            print(f"Invalid number of tickets. You can buy up to {ticket_limit} tickets at a time.")
            continue

        # Check if there are enough tickets available
        if tickets_requested > total_tickets:
            print(f"Sorry, there are only {total_tickets} tickets left.")
            continue

        # Deduct the number of tickets purchased from the total tickets
        total_tickets -= tickets_requested
        total_buyers += 1  # Increment the number of buyers

        # Display the number of remaining tickets
        print(f"Tickets purchased: {tickets_requested}")
        print(f"Remaining tickets: {total_tickets}")

    # Display the total number of buyers
    print(f"All tickets have been sold. Total number of buyers: {total_buyers}")

# Call the main function to start the application
if __name__ == "__main__":
    main()

