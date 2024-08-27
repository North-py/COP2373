import random

def get_responses_from_file(ball_responses):
    with open(ball_responses, 'r') as file:
        responses = [line.strip() for line in file]
    return responses

def magic_8_ball():
    responses = get_responses_from_file('8ball_responses.txt')
    
    while True:
        question = input("Ask a yes/no question (or type 'quit' to exit): ")
        if question.lower() == 'quit':
            print("Goodbye!")
            break
        
        # Randomly select a response
        response = random.choice(responses)
        print(response)

# Run the Magic 8 Ball program
magic_8_ball()
