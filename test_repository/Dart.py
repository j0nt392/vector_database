def play_dart_game():
    score = 501
    throws = 0
    while score > 0:
        print(f'Current score: {score}')
        print('Enter your throw (e.g., 20, T20, D20): ')
        throw = input().upper()
        if throw.startswith('T'):
            multiplier = 3
            number = int(throw[1:])
        elif throw.startswith('D'):
            multiplier = 2
            number = int(throw[1:])
        else:
            multiplier = 1
            number = int(throw)
        points = multiplier * number
        score -= points
        throws += 1
        if score < 0:
            score += points
            throws -= 1
            print('Invalid throw! Try again.')
    print(f'Congratulations! You won in {throws} throws.')

# Call the play_dart_game function
play_dart_game()

# Print congratulations message
congrats_message = f"Congratulations! You won in {throws} throws."
print(congrats_message)

# Print current score
current_score_message = f"Current score: {score}"
print(current_score_message)

# Print prompt for input
input_message = "Enter your throw (e.g., 20, T20, D20): "
print(input_message)

# Print invalid throw message
invalid_throw_message = "Invalid throw! Try again."
print(invalid_throw_message)