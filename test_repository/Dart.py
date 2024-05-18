def play_dart_game():
    # Set the initial score to 501 and the number of throws to 0
    score = 501
    throws = 0

    # Loop until the score reaches 0
    while score > 0:
        # Display the current score and prompt for the throw
        print(f'Current score: {score}')
        throw_input = input('Enter your throw (e.g., 20, T20, D20): ').upper()
        
        # Check if the throw is a single, double, or triple
        if throw_input.startswith('T'):
            multiplier = 3
            number = int(throw_input[1:])
        elif throw_input.startswith('D'):
            multiplier = 2
            number = int(throw_input[1:])
        else:
            multiplier = 1
            number = int(throw_input)
        
        # Calculate the points and update the score and number of throws
        points = multiplier * number
        score -= points
        throws += 1
        
        # If the score goes below 0, undo the last throw and display an error message
        if score < 0:
            score += points
            throws -= 1
            print('Invalid throw! Try again.')
    
    # Display the final score and the number of throws it took to win
    print(f'Congratulations! You won in {throws} throws.')

play_dart_game()